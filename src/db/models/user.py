"""User model file."""
import datetime
import enum
from typing import List
import sqlalchemy as sa
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Role(enum.IntEnum):
    """You can change these roles as you want."""

    USER = 0
    MODERATOR = 1
    ADMINISTRATOR = 2

    
class User(Base):
    """User model."""

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, nullable=False
    )
    user_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    first_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    second_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    role: Mapped[Role] = mapped_column(sa.Enum(Role), default=Role.USER)
