import os
from openai import OpenAI
from app.core.config import settings


class GeminiClient:
    """
    Thin client wrapper around Gemini (OpenAI-compatible API).

    Responsibility:
    - Accept prompt
    - Return generated text
    - No business logic
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url=settings.GEMINI_API_URL,
        )

        self.model = "gemini-2.5-flash-lite"

    async def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content
