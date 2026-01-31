from pypdf import PdfReader
from .base import BaseExtractor

class TextExtractor(BaseExtractor):
    async def extract_text(self, file_bytes: bytes) -> str:
        return file_bytes.decode('utf-8', errors='ignore')
