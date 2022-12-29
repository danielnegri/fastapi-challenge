from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, service, storage
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Loan])
def list(
    db: Session = Depends(deps.get_db),
    page: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve loans.
    """
    loans = service.loans.get_multi_by_user(
        db, user_id=current_user.id, page=page, limit=limit
    )
    return loans


@router.get("/{loan_id}", response_model=schemas.Loan)
def get(
    loan_id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific loan by id.
    """
    loan = service.loans.get(db, id=loan_id)
    if loan.user_id == current_user.id:
        return loan
    if not storage.users.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
        )
    return loan


@router.post("/", response_model=schemas.Loan, status_code=status.HTTP_201_CREATED)
def create(
    *,
    db: Session = Depends(deps.get_db),
    loan_in: schemas.LoanCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new loan.
    """
    loan_in.user_id = current_user.id
    loan = service.loans.create(db, obj_in=loan_in)
    return loan


@router.put("/{loan_id}", response_model=schemas.Loan)
def update(
    *,
    db: Session = Depends(deps.get_db),
    loan_id: str,
    loan_in: schemas.LoanUpdate,
    _: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a loan.
    """
    loan = service.loans.get(db, id=loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan not found",
        )
    user = service.loans.update(db, db_obj=loan, obj_in=loan_in)
    return user
