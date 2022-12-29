from sqlalchemy.orm import Session

from app import storage
from app.core.config import settings
from app.models import User
from app.schemas import UserCreate
from app.tests.utils.random import random_email, random_lower_string


def create_random_user(db: Session) -> User:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(username=email, email=email, password=password)
    user = storage.users.create(db=db, obj_in=user_in)
    return user


def create_superuser(db: Session) -> User:
    superuser = storage.users.get_by_email(db, email=settings.ADMIN_EMAIL)
    if not superuser:
        user_in = UserCreate(
            email=settings.ADMIN_EMAIL,
            password=settings.ADMIN_PASSWORD,
            full_name="Administrator",
            is_superuser=True,
        )
        superuser = storage.users.create(db, obj_in=user_in)

    return superuser
