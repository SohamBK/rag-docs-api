from sqlalchemy.ext.asyncio import AsyncEngine
from app.core.logging import logger
from app.infrastructure.db.base import Base

async def init_db(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.create_all)
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
