from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.models.base import Base

if TYPE_CHECKING:
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    loans = relationship("Loan")
