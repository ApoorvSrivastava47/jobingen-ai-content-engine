from openai import OpenAI

from app.clients.base_client import BaseAIClient
from app.config.config import Config


class OpenAIClient(BaseAIClient):
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:

        response = self.client.responses.create(
            model=Config.DEFAULT_MODEL,
            temperature=temperature,
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return response.output_text
