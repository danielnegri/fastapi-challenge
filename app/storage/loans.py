import secrets
from typing import Any, Dict, List, Union

from sqlalchemy.orm import Session

from app.models import Loan
from app.schemas import LoanCreate, LoanUpdate
from app.storage.base import Base


class LoansStorage(Base[Loan, LoanCreate, LoanUpdate]):
    def create(self, db: Session, *, obj_in: LoanCreate, user_id: str) -> Loan:
        db_obj = self.model(
            id=f"u_{secrets.token_hex(6)}",
            user_id=user_id,
            title=obj_in.title,
            amount_cents=obj_in.amount_cents,
            annual_interest_rate=obj_in.annual_interest_rate,
            currency=obj_in.currency,
            term_months=obj_in.term_months,
            due_monthly_starting=obj_in.due_monthly_starting,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Loan, obj_in: Union[LoanUpdate, Dict[str, Any]]
    ) -> Loan:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi_by_user(
        self, db: Session, *, user_id: int, page: int = 0, limit: int = 100
    ) -> List[Loan]:
        offset = page * limit
        return (
            db.query(self.model)
            .filter(Loan.user_id == user_id)
            .order_by(Loan.created_at.asc())
            .offset(offset)
            .limit(limit)
            .all()
        )


loans = LoansStorage(Loan)
