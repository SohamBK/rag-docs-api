from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.api import api_router

from app.infrastructure.db.session import engine
from app.infrastructure.db.init_db import init_db

from app.core.responses import ErrorResponse, ErrorDetail
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import AppException

logger = setup_logging()

app = FastAPI(
    title=settings.app_name,
    docs_url="/docs" if settings.environment == "development" else None,
    redoc_url="/redoc" if settings.environment == "development" else None,
)

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    """
    Handles all known, expected application errors.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=ErrorDetail(
                code=exc.error_code,
                message=exc.message,
            )
        ).model_dump(),
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """
    Handles unexpected errors safely (no stacktrace leakage).
    """
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error=ErrorDetail(
                code="INTERNAL_SERVER_ERROR",
                message="An unexpected error occurred",
            )
        ).model_dump(),
    )

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up")
    try:
        await init_db(engine)
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
    logger.info("Database initialized")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")

app.include_router(api_router, prefix="/api/v1")