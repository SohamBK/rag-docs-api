from sqlalchemy import ForeignKey, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

from pgvector.sqlalchemy import Vector

from app.infrastructure.db.base import Base

class Embedding(Base):
    __tablename__ = "embeddings"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    document_id: Mapped[UUID] = mapped_column(
        ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    embedding: Mapped[list[float]] = mapped_column(
        Vector(384),
        nullable=False,
    )

    metadata_info: Mapped[dict] = mapped_column(
        JSON,
        nullable=True,
    )

    document = relationship(
        "Document",
        back_populates="embeddings",
    )
