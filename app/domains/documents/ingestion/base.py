from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    async def extract_text(self, file_bytes: bytes) -> str:
        """
        Extract raw text from a document.
        Must return plain text.
        """
        raise NotImplementedError
