import datetime
import enum

from sqlalchemy import BigInteger, Column, Date, Enum, ForeignKey, Integer, String

from app.models.base import Base


class ScheduleStatus(enum.Enum):
    SCHEDULED = "scheduled"
    PAID = "paid"
    CANCELED = "canceled"
    DUE = "due"


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(String(), primary_key=True)
    loan_id = Column(String(), ForeignKey("loans.id"))
    month = Column(Integer(), default=1, nullable=False)
    due = Column(Date(), default=datetime.date.today(), nullable=False)
    amount_cents = Column(BigInteger(), default=0, nullable=False)  # Monthly payment
    principal_cents = Column(BigInteger(), default=0, nullable=False)
    interest_cents = Column(BigInteger(), default=0, nullable=False)
    balance_cents = Column(BigInteger(), default=0, nullable=False)
    status = Column(
        Enum(ScheduleStatus), default=ScheduleStatus.SCHEDULED, nullable=False
    )
