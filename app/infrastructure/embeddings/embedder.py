from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Responsible ONLY for generating embeddings.
    No database logic.
    No business logic.
    """

    def __init__(self):
        # Loaded once per process
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_query(self, text: str) -> list[float]:
        """
        Embed a user query.
        """
        return self.model.encode(text).tolist()

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """
        Embed multiple document chunks.
        """
        return self.model.encode(texts).tolist()
