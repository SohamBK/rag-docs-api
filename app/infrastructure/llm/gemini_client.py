from openai import OpenAI
from app.core.config import settings


class GeminiClient:
    """
    Gemini client using OpenAI-compatible API.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url=settings.GEMINI_API_URL,
        )
        self.model = "gemini-2.5-flash-lite"

    async def generate(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()
