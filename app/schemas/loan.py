from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, condecimal

decimal_type = condecimal(ge=0, max_digits=15, decimal_places=5)


class LoanBase(BaseModel):
    title: Optional[str] = None
    amount_cents: Optional[PositiveInt] = None
    annual_interest_rate: Optional[decimal_type] = None
    currency: Optional[str] = "USD"
    term_months: Optional[int] = None
    due_monthly_starting: Optional[date] = None
    is_active: Optional[bool] = True


class LoanCreate(LoanBase):
    title: str
    amount_cents: PositiveInt
    annual_interest_rate: decimal_type
    term_months: PositiveInt
    due_monthly_starting: date


class LoanUpdate(BaseModel):
    title: Optional[str]
    is_active: Optional[bool]
    currency: Optional[str]


class LoanInDBBase(LoanBase):
    id: Optional[str]
    user_id: Optional[str]

    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Loan(LoanInDBBase):
    pass


class LoanInDB(LoanInDBBase):
    pass
