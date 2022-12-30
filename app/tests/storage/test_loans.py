import datetime
import random

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import storage
from app.models import User
from app.schemas import LoanCreate
from app.tests.utils.random import random_decimal, random_lower_string
from app.utils import nth_day_of_next_month


def random_loan_create(user_id: str) -> LoanCreate:
    title = random_lower_string()
    amount_cents = random.randint(100, 1_000_000_000)
    annual_interest_rate = random_decimal()
    term_months = random.randint(12, 12 * 35)
    due_monthly_starting = nth_day_of_next_month(datetime.datetime.utcnow(), 15)
    return LoanCreate(
        user_id=user_id,
        title=title,
        amount_cents=amount_cents,
        annual_interest_rate=annual_interest_rate,
        term_months=term_months,
        due_monthly_starting=due_monthly_starting,
    )


def test_create_loan(db: Session, random_user: User) -> None:
    obj_in = random_loan_create(random_user.id)
    loan = storage.loans.create(db, obj_in=obj_in)
    assert loan
    assert loan.user_id == random_user.id
    assert loan.currency == "USD"


def test_update_loan(db: Session, random_user: User) -> None:
    loan = storage.loans.create(db, obj_in=random_loan_create(random_user.id))
    obj_in = random_loan_create(random_user.id)
    loan_1 = storage.loans.update(db, db_obj=loan, obj_in=obj_in)
    assert loan_1.id == loan.id
    assert loan_1.user_id == loan.user_id
    assert loan_1.amount_cents == obj_in.amount_cents
    assert loan_1.annual_interest_rate == obj_in.annual_interest_rate
    assert loan_1.term_months == obj_in.term_months


def test_get_loan(db: Session, random_user: User) -> None:
    loan = storage.loans.create(db, obj_in=random_loan_create(random_user.id))
    loan_2 = storage.loans.get(db, id=loan.id)
    assert loan_2
    assert loan.user_id == loan_2.user_id
    assert jsonable_encoder(loan) == jsonable_encoder(loan_2)


def test_get_multi_by_user(db: Session, random_user: User) -> None:
    loan_1 = storage.loans.create(db, obj_in=random_loan_create(random_user.id))
    loan_2 = storage.loans.create(db, obj_in=random_loan_create(random_user.id))
    loans = storage.loans.get_multi_by_user(db, user_id=random_user.id)
    assert len(loans) == 2
    assert jsonable_encoder(loans) == jsonable_encoder([loan_1, loan_2])
