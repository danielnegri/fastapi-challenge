from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, NonNegativeInt, PositiveInt, condecimal, constr

decimal_type = condecimal(ge=0, max_digits=15, decimal_places=5)
user_id_type = constr(strip_whitespace=True, min_length=8)


class LoanBase(BaseModel):
    user_id: Optional[user_id_type] = None
    title: Optional[str] = None
    amount_cents: Optional[NonNegativeInt] = None
    annual_interest_rate: Optional[decimal_type] = None
    currency: Optional[str] = "USD"
    term_months: Optional[int] = None
    due_monthly_starting: Optional[date] = None
    is_active: Optional[bool] = True


class LoanCreate(LoanBase):
    user_id: user_id_type
    title: str
    amount_cents: NonNegativeInt
    annual_interest_rate: decimal_type
    term_months: PositiveInt
    due_monthly_starting: date


class LoanUpdate(BaseModel):
    title: Optional[str]
    is_active: Optional[bool]
    currency: Optional[str]


class LoanInDBBase(LoanBase):
    id: Optional[str] = None

    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Loan(LoanInDBBase):
    pass


class LoanInDB(LoanInDBBase):
    pass
