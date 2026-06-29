from ollama import chat

from app.clients.base_client import BaseAIClient


class LlamaClient(BaseAIClient):
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:

        response = chat(
            model="llama3.2",
            messages=[
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

        return response["message"]["content"]
