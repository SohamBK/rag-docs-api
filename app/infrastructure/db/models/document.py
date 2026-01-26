from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from uuid import uuid4, UUID

from app.infrastructure.db.base import Base

class Document(Base):
    __tablename__ = "documents"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )

    source: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    title: Mapped[str | None] = mapped_column(
        String(length=255),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )

    embeddings = relationship(
        "Embedding",
        back_populates="document",
        cascade="all, delete-orphan",
    )
