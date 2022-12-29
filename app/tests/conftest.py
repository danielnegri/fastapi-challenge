from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.main import app
from app.models.session import SessionLocal
from app.tests.utils.auth import (
    authentication_token_from_email,
    get_superuser_token_headers,
)
from app.tests.utils.users import create_random_user, create_superuser


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="session")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def random_user(db: Session):
    return create_random_user(db)


@pytest.fixture(scope="session", autouse=True)
def superuser(db: Session):
    return create_superuser(db)


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> Dict[str, str]:
    return get_superuser_token_headers(client)


@pytest.fixture(scope="module")
def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return authentication_token_from_email(
        client=client, email=settings.EMAIL_TEST_USER, db=db
    )
