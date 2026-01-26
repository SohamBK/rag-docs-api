from pydantic import BaseModel, Field
from typing import Optional

class DocumentCreate(BaseModel):
    source: str = Field(..., description="Document source or filename")
    title: Optional[str] = Field(None, description="Human-readable title")
    content: str = Field(..., description="Raw document text")

class DocumentChunk(BaseModel):
    content: str
    index: int