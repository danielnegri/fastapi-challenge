from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import storage
from app.core.config import settings
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.random import random_lower_string


def user_authentication_headers(
    *, client: TestClient, email: str, password: str
) -> Dict[str, str]:
    data = {"username": email, "password": password}

    r = client.post(f"{settings.API_V1_PREFIX}/auth/token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email(
    *, client: TestClient, email: str, db: Session
) -> Dict[str, str]:
    """
    Return a valid token for the user with given email.

    If the user doesn't exist it is created first.
    """
    password = random_lower_string()
    user = storage.users.get_by_email(db, email=email)
    if not user:
        user_in_create = UserCreate(username=email, email=email, password=password)
        user = storage.users.create(db, obj_in=user_in_create)
    else:
        user_in_update = UserUpdate(password=password)
        user = storage.users.update(db, db_obj=user, obj_in=user_in_update)

    return user_authentication_headers(client=client, email=email, password=password)


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.ADMIN_EMAIL,
        "password": settings.ADMIN_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_PREFIX}/auth/token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
