from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, NonNegativeInt, PositiveInt, constr

from app.models import ScheduleStatus

loan_id_type = constr(strip_whitespace=True, min_length=8)


class ScheduleBase(BaseModel):
    loan_id: Optional[loan_id_type]
    month: Optional[PositiveInt]
    due: Optional[date]
    amount_cents: Optional[NonNegativeInt] = None
    interest_cents: Optional[NonNegativeInt] = None
    principal_cents: Optional[NonNegativeInt] = None
    balance_cents: Optional[NonNegativeInt] = None
    status: Optional[str] = ScheduleStatus.SCHEDULED


class ScheduleCreate(ScheduleBase):
    loan_id: loan_id_type
    month: PositiveInt
    due: date
    amount_cents: NonNegativeInt
    interest_cents: NonNegativeInt
    principal_cents = NonNegativeInt
    balance_cents: NonNegativeInt


class ScheduleUpdate(BaseModel):
    status: Optional[str]


class ScheduleInDBBase(ScheduleBase):
    id: Optional[str]

    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Schedule(ScheduleInDBBase):
    pass


class ScheduleInDB(ScheduleInDBBase):
    pass
