from fastapi import APIRouter, Depends
from app.core.responses import SuccessResponse
from app.domains.rag.service import RAGService

from app.api.deps.db import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/query")
async def query_rag(
    question: str,
    db: AsyncSession = Depends(get_db_session),
):
    result = await RAGService.answer(db, question)

    return SuccessResponse(
        data=result,
        message="Answer generated using RAG",
    )

