SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer the user's question using ONLY the provided context.
If the answer is not present in the context, say:
"I don't have enough information to answer this question."
"""

def build_rag_prompt(context: str, question: str) -> str:
    return f"""
Context:
{context}

Question:
{question}

Answer:
"""
