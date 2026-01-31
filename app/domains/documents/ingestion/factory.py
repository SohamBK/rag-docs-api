from fastapi import UploadFile
from .pdf import PDFExtractor
from .txt import TextExtractor


def get_extractor(file: UploadFile):
    if file.content_type == "application/pdf":
        return PDFExtractor()

    if file.content_type == "text/plain":
        return TextExtractor()

    raise ValueError(f"Unsupported file type: {file.content_type}")
