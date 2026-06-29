from google import genai

from app.clients.base_client import BaseAIClient
from app.config.settings import settings


class GeminiClient(BaseAIClient):
    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )

        self.model = settings.GEMINI_MODEL

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:

        prompt = f"""
SYSTEM:

{system_prompt}


USER:

{user_prompt}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text
