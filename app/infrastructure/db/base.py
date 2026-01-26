from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from app.infrastructure.db.models.document import Document
from app.infrastructure.db.models.embedding import Embedding
