from sqlalchemy.ext.asyncio import AsyncEngine

from app.infrastructure.db.base import Base
from app.infrastructure.db.models import Document, Embedding

async def init_db(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)