from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.api.deps.db import get_db_session
from app.core.responses import SuccessResponse, ErrorResponse

router = APIRouter(
    prefix="/health",
    tags=["Health Check"],
)

@router.get("/", response_model=SuccessResponse[None])
async def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return SuccessResponse(
        data=None,
        message="API is healthy"
    )

@router.get("/db-health", response_model=SuccessResponse[None])
async def db_health_check(db: AsyncSession = Depends(get_db_session)):
    """
    Health check endpoint to verify database connectivity.
    """
    try:
        await db.execute(text("SELECT 1"))
        return SuccessResponse(
            data=None,
            message="Database connection is healthy"
        )
    except Exception as e:
        return ErrorResponse(
            data=None,
            message=f"Database connection failed: {str(e)}"
        )
