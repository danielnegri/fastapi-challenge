from sqlalchemy import DECIMAL, BigInteger, Column, ForeignKey, Integer, String

from app.models.base import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(String, primary_key=True)
    loan_id = Column(String, ForeignKey("loans.id"))
    # loan = relationship("Loan", back_populates="loan")
    month = Column(Integer, default=0, nullable=False)
    # Monthly payment
    amount_cents = Column(BigInteger(), default=0, nullable=False)
    interest = Column(DECIMAL(15, 5), default=0, nullable=False)
    balance_cents = Column(DECIMAL(15, 5), default=0, nullable=False)
