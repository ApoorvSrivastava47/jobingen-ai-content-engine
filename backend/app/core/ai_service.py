from app.clients.factory import AIClientFactory


class AIService:
    def __init__(self):
        self.client = AIClientFactory.create()

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:

        return self.client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=temperature,
        )
