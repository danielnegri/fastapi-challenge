from datetime import datetime

from sqlalchemy.orm import Session

from app import service, storage
from app.models import User
from app.schemas import LoanCreate
from app.tests.utils.random import random_lower_string
from app.utils import nth_day_of_next_month


def test_create_loan_and_schedules(db: Session, random_user: User) -> None:
    title = random_lower_string()
    amount_cents = 100_000_00
    annual_interest_rate = 1.0
    term_months = 3
    due_monthly_starting = nth_day_of_next_month(datetime.utcnow(), 1)
    obj_in = LoanCreate(
        user_id=random_user.id,
        title=title,
        amount_cents=amount_cents,
        annual_interest_rate=annual_interest_rate,
        term_months=term_months,
        due_monthly_starting=due_monthly_starting,
    )

    loan = service.loans.create(db, obj_in=obj_in)
    assert loan
    assert loan.user_id == random_user.id
    assert loan.currency == "USD"

    # check schedule
    # month, amortization_amount, interest, principal, balance
    expected = (
        (1, 3903696, 833333, 3070362, 6929638),
        (2, 3903696, 577470, 3326226, 3603411),
        (3, 3903696, 300284, 3603411, 0),
    )

    schedule = storage.schedules.get_multi_by_loan(db, loan_id=loan.id)
    assert len(schedule) == term_months

    for idx, loan_schedule in enumerate(schedule):
        expected_values = expected[idx]
        assert loan_schedule.month == expected_values[0]
        assert loan_schedule.amount_cents == expected_values[1]
        assert loan_schedule.interest_cents == expected_values[2]
        assert loan_schedule.principal_cents == expected_values[3]
        assert loan_schedule.balance_cents == expected_values[4]
