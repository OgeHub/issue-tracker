from __future__ import annotations

import uuid

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from issue_tracker.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    photo: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
        default=None,
    )
    password: Mapped[str] = mapped_column(String(200), nullable=False)

    issues: Mapped[list["Issue"]] = relationship(back_populates="author")
    
    