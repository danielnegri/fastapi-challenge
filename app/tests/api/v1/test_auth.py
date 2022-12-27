from fastapi import status
from fastapi.testclient import TestClient

from app.core.config import settings


def test_access_token(client: TestClient) -> None:
    login_data = {
        "username": settings.ADMIN_EMAIL,
        "password": settings.ADMIN_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_PREFIX}/auth/token", data=login_data)
    tokens = r.json()
    assert r.status_code == status.HTTP_201_CREATED
    assert "access_token" in tokens
    assert tokens["access_token"]
