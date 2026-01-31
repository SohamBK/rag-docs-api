from typing import List
from app.domains.documents.schemas import DocumentChunk


class TextChunker:
    """
    Splits text into overlapping chunks.
    """

    def __init__(self, chunk_size: int = 600, overlap: int = 100):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[DocumentChunk]:
        chunks: List[DocumentChunk] = []
        start = 0
        index = 0
        text_length = len(text)

        while start < text_length:
            end = start + self.chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    DocumentChunk(
                        content=chunk_text,
                        index=index,
                    )
                )
                index += 1

            start = end - self.overlap

        return chunks
