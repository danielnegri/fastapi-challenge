import datetime

from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import storage
from app.core.config import settings
from app.tests.utils.random import random_lower_string


def test_create_loan(
    client: TestClient, normal_user_token_headers: dict, db: Session
) -> None:
    user = storage.users.get_by_email(db, email=settings.EMAIL_TEST_USER)
    data = {
        "user_id": user.id,
        "title": random_lower_string(),
        "amount_cents": 300_00,
        "annual_interest_rate": 0,
        "currency": "CAD",
        "term_months": 3,
        "due_monthly_starting": datetime.date.today().isoformat(),
    }

    r = client.post(
        f"{settings.API_V1_PREFIX}/loans/", headers=normal_user_token_headers, json=data
    )

    assert r.status_code == status.HTTP_201_CREATED
