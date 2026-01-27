from pydantic import BaseModel
from typing import List, Optional, Dict
from uuid import UUID

class RetrievalResult(BaseModel):
    document_id: UUID
    content: str
    score: float
    metadata: Optional[Dict]

    class Config:
        from_attributes = True
