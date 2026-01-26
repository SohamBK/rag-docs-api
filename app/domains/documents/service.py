from uuid import UUID
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.documents.schemas import DocumentCreate
from app.domains.documents.chunker import TextChunker
from app.infrastructure.db.models.document import Document
from app.infrastructure.repositories.embedding_repo import EmbeddingRepository
from app.infrastructure.embeddings.sentence_transformer import (
    SentenceTransformerEmbedding,
)


class DocumentService:
    """
    Orchestrates document ingestion.
    """

    @staticmethod
    async def ingest_document(
        db: AsyncSession,
        payload: DocumentCreate,
    ) -> UUID:
        # 1. Create document record
        document = Document(
            source=payload.source,
            title=payload.title,
        )
        db.add(document)
        await db.commit()
        await db.refresh(document)

        # 2. Chunk document
        chunker = TextChunker()
        chunks = chunker.chunk(payload.content)

        chunk_texts: List[str] = [c.content for c in chunks]
        chunk_metadata = [
            {
                "chunk_index": c.index,
                "source": payload.source,
            }
            for c in chunks
        ]

        # 3. Generate embeddings
        embedder = SentenceTransformerEmbedding()
        embeddings = embedder.embed(chunk_texts)

        # 4. Persist embeddings
        await EmbeddingRepository.bulk_create(
            db=db,
            document_id=document.id,
            chunks=chunk_texts,
            embeddings=embeddings,
            metadata=chunk_metadata,
        )

        return document.id