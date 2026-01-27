from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.embeddings.embedder import EmbeddingService
from app.infrastructure.repositories.embedding_repo import EmbeddingRepository
from app.infrastructure.llm.gemini_client import GeminiClient
from app.domains.rag.prompt import build_rag_prompt
from app.domains.rag.schemas import RetrievalResult


class RAGService:
    llm = GeminiClient()
    embedder = EmbeddingService()

    @staticmethod
    async def retrieve(db, question: str):
        query_embedding = RAGService.embedder.embed_query(question)

        rows = await EmbeddingRepository.similarity_search(
            db=db,
            query_embedding=query_embedding,
        )

        # ✅ Explicit mapping
        return [
            RetrievalResult(
                document_id=row.document_id,
                content=row.content,
                score=0.0,
                metadata=row.metadata_info,
            )
            for row in rows
        ]

    @staticmethod
    async def answer(db: AsyncSession, question: str):
        results = await RAGService.retrieve(db, question)

        if not results:
            return {
                "answer": "I don't know based on the provided context.",
                "sources": []
            }

        contexts = [r.content for r in results]
        prompt = build_rag_prompt(question, contexts)
        answer = await RAGService.llm.generate(prompt)

        return {
            "answer": answer,
            "sources": results
        }
