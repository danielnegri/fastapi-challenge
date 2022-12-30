from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, service, storage
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Schedule])
def list_schedule(
    *,
    db: Session = Depends(deps.get_db),
    loan_id: str,
    page: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> List[schemas.Schedule]:
    """
    Retrieve loan schedule.
    """
    loan = service.loans.get(db, id=loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan not found",
        )

    if loan.user_id != current_user.id and not storage.users.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
        )

    schedules = storage.schedules.get_multi_by_loan(
        db, loan_id=loan_id, page=page, limit=limit
    )
    return schedules
