import io
from pypdf import PdfReader
from .base import BaseExtractor


class PDFExtractor(BaseExtractor):
    async def extract_text(self, file_bytes: bytes) -> str:
        reader = PdfReader(io.BytesIO(file_bytes))

        pages = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text)

        return "\n".join(pages)
