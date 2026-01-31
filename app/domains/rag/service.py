from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.embeddings.embedder import EmbeddingService
from app.infrastructure.repositories.embedding_repo import EmbeddingRepository
from app.infrastructure.llm.gemini_client import GeminiClient
from app.domains.rag.prompt import SYSTEM_PROMPT, build_rag_prompt
from app.domains.rag.schemas import RetrievalResult
from app.infrastructure.embeddings.sentence_transformer import (
    SentenceTransformerEmbedding,
)

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
        embedder = SentenceTransformerEmbedding()
        query_embedding = embedder.embed([question])[0]

        results = await EmbeddingRepository.similarity_search(
            db=db,
            query_embedding=query_embedding,
            limit=5,
        )

        if not results:
            return {
                "answer": "I don't have enough information to answer this question.",
                "sources": [],
            }

        # 3. Build context
        context = "\n\n".join(f"- {r.content}" for r in results)

        # 4. Call LLM
        llm = GeminiClient()
        answer = await llm.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=build_rag_prompt(context, question),
        )

        return {
            "answer": answer,
            "sources": [
                {
                    "document_id": r.document_id,
                    "metadata": r.metadata_info,
                }
                for r in results
            ],
        }