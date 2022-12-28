from typing import Optional

from pydantic import BaseModel, PositiveInt, condecimal

decimal_type = condecimal(ge=0, max_digits=15, decimal_places=5)


class LoanBase(BaseModel):
    amount_cents: Optional[PositiveInt] = None
    annual_interest_rate: Optional[decimal_type] = None
    currency: Optional[str] = "USD"
    term_months: Optional[int] = None


class LoanCreate(LoanBase):
    amount_cents: PositiveInt
    annual_interest_rate: decimal_type
    term_months: PositiveInt


class LoanUpdate(LoanBase):
    pass


class LoanInDBBase(LoanBase):
    id: str
    user_id: str

    class Config:
        orm_mode = True


class Loan(LoanInDBBase):
    pass


class LoanInDB(LoanInDBBase):
    pass
