import datetime
from typing import AnyStr

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    id: AnyStr

    created_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
