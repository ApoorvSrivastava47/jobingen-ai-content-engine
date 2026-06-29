from app.clients.providers.llama_client import LlamaClient
from app.clients.providers.gemini_client import GeminiClient

from app.config.settings import settings


class AIClientFactory:
    @staticmethod
    def create():

        provider = settings.LLM_PROVIDER.lower()

        if provider == "ollama":
            return LlamaClient()

        elif provider == "gemini":
            return GeminiClient()

        else:
            raise ValueError(f"Unsupported provider: {provider}")
