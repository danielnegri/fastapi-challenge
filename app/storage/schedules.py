import secrets
from typing import Any, Dict, List, Union

from sqlalchemy.orm import Session

from app.models import Schedule, ScheduleStatus
from app.schemas import ScheduleCreate, ScheduleUpdate
from app.storage.base import Base


class SchedulesStorage(Base[Schedule, ScheduleCreate, ScheduleUpdate]):
    def create(self, db: Session, *, obj_in: ScheduleCreate) -> Schedule:
        db_obj = self.model(
            id=f"ls_{secrets.token_hex(6)}",
            loan_id=obj_in.loan_id,
            month=obj_in.month,
            due=obj_in.due,
            amount_cents=obj_in.amount_cents,
            interest_cents=obj_in.interest_cents,
            principal_cents=obj_in.principal_cents,
            balance_cents=obj_in.balance_cents,
            status=ScheduleStatus.SCHEDULED,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Schedule,
        obj_in: Union[ScheduleUpdate, Dict[str, Any]],
    ) -> Schedule:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi_by_loan(
        self, db: Session, *, loan_id: int, page: int = 0, limit: int = 100
    ) -> List[Schedule]:
        offset = page * limit
        return (
            db.query(self.model)
            .filter(Schedule.loan_id == loan_id)
            .order_by(Schedule.month.asc())
            .offset(offset)
            .limit(limit)
            .all()
        )


schedules = SchedulesStorage(Schedule)
