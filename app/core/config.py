import os
import secrets

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    API_V1_PREFIX: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    # 60 minutes * 24 hours * 15 days = 15 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 15

    PROJECT_NAME: str = "FastAPI Challenge"

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "SQLALCHEMY_DATABASE_URI", f"sqlite:///challenge-{ENVIRONMENT}.sqlite3"
    )

    ADMIN_EMAIL: EmailStr = os.getenv("ADMIN_EMAIL", "admin@example.com")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "admin")
    EMAIL_TEST_USER: EmailStr = "test@example.com"

    class Config:
        case_sensitive = True


settings = Settings()
