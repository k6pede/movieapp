import datetime
from sqlalchemy import Boolean, Column, String, DateTime, CHAR

from database import Base
from pydantic import BaseModel
from typing import Optional


class UserOrm(Base):
    __tablename__ = "users"

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
    )
    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )


class User(BaseModel):
    id = str
    email = str
    is_active = bool
    created_at = datetime.datetime
    updated_at = datetime.datetime
    deleted_at = Optional[datetime.datetime]

    class Config:
        orm_mode = True
