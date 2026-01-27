from typing import List


def build_rag_prompt(question: str, contexts: List[str]) -> str:
    """
    Builds a strict RAG prompt to minimize hallucinations.
    """

    context_block = "\n\n".join(contexts)

    return f"""
You are a helpful backend engineering assistant.

Use ONLY the context below to answer the question.
If the answer is not present, say: "I don't know based on the provided context."

Context:
{context_block}

Question:
{question}

Answer concisely and clearly:
""".strip()
