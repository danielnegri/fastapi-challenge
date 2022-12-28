import datetime

from sqlalchemy import (
    DECIMAL,
    BigInteger,
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
)

from .base import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    amount_cents = Column(BigInteger(), default=0, nullable=False)
    annual_interest_rate = Column(DECIMAL(15, 5), default=0, nullable=False)
    currency = Column(String, default="USD", nullable=False)
    term_months = Column(Integer, default=0, nullable=False)
    due_monthly_starting = Column(Date(), default=datetime.date.today(), nullable=False)
    is_active = Column(Boolean(), default=True)
