from typing import List
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.embedding import Embedding


class EmbeddingRepository:
    """
    Handles persistence of embeddings.
    """

    @staticmethod
    async def bulk_create(
        db: AsyncSession,
        document_id: UUID,
        chunks: List[str],
        embeddings: List[List[float]],
        metadata: List[dict],
    ) -> None:
        records = [
            Embedding(
                document_id=document_id,
                content=chunk,
                embedding=embedding,
                metadata=meta,
            )
            for chunk, embedding, meta in zip(chunks, embeddings, metadata)
        ]

        db.add_all(records)
        await db.commit()
