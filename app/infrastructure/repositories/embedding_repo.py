from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models.embedding import Embedding


class EmbeddingRepository:
    """
    Handles persistence and retrieval of embeddings.
    """

    @staticmethod
    async def bulk_create(
        db: AsyncSession,
        document_id,
        chunks,
        embeddings,
        metadata,
    ) -> None:
        records = [
            Embedding(
                document_id=document_id,
                content=chunk,
                embedding=embedding,
                metadata_info=meta,
            )
            for chunk, embedding, meta in zip(chunks, embeddings, metadata)
        ]
        db.add_all(records)
        await db.commit()

    @staticmethod
    async def similarity_search(
        db: AsyncSession,
        query_embedding: List[float],
        limit: int = 5,
    ) -> List[Embedding]:
        stmt = (
            select(Embedding)
            .order_by(Embedding.embedding.cosine_distance(query_embedding))
            .limit(limit)
        )

        result = await db.execute(stmt)
        return result.scalars().all()