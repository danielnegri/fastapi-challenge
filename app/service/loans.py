import logging
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session

from app import storage
from app.models import Loan
from app.schemas import LoanCreate, LoanUpdate, ScheduleCreate
from app.service.base import BaseService

from ..utils import nth_day_of_next_month
from .amortization import amortization_schedule

logger = logging.getLogger(__name__)


class LoanService(BaseService):
    @staticmethod
    def create(db: Session, *, obj_in: LoanCreate) -> Loan:
        logger.info(f"Creating loan: obj_in={obj_in}")
        db.begin_nested()
        loan = storage.loans.create(db, obj_in=obj_in)

        starting = loan.due_monthly_starting
        due = datetime(year=starting.year, month=starting.month, day=starting.day)
        for period, amount, interest, principal, balance in amortization_schedule(
            principal=obj_in.amount_cents,
            annual_interest_rate=float(obj_in.annual_interest_rate),
            period=obj_in.term_months,
        ):
            # Create n (term months) of schedules
            schedule_in = ScheduleCreate(
                loan_id=loan.id,
                month=period,
                due=due,
                amount_cents=round(amount),
                interest_cents=round(interest),
                principal_cents=round(principal),
                balance_cents=round(balance),
            )
            storage.schedules.create(db, obj_in=schedule_in)
            due = nth_day_of_next_month(due, due.day)

        db.commit()
        return loan

    @staticmethod
    def update(
        self, db: Session, *, db_obj: Loan, obj_in: Union[LoanUpdate, Dict[str, Any]]
    ) -> Loan:
        logger.info(f"Updating loan: user_id={db_obj.user_id}")
        return storage.loans.update(db, db_obj=db_obj, obj_in=obj_in)

    @staticmethod
    def get(self, db: Session, id: str) -> Optional[Loan]:
        logger.info(f"Fetching loan: loan_id={id}")
        return storage.loans.get(db, id=id)

    @staticmethod
    def list(
        self, db: Session, *, user_id: int, page: int = 0, limit: int = 100
    ) -> List[Loan]:
        logger.info(f"Listing loans: user_id={user_id}, page={page}, limit={limit}")
        return storage.loans.get_multi_by_user(
            db, user_id=user_id, page=page, limit=limit
        )


loans = LoanService(BaseService)
