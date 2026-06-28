from app.clients.base_client import BaseAIClient


class MockClient(BaseAIClient):
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:

        return f"""
========== MOCK RESPONSE ==========

SYSTEM:

{system_prompt}

----------------------------------

USER:

{user_prompt}

Temperature: {temperature}

==================================
"""
