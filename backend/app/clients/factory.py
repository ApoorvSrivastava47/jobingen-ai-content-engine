from loguru import logger

from app.clients.providers.llama_client import LlamaClient
from app.clients.providers.gemini_client import GeminiClient
from app.clients.providers.openai_client import OpenAIClient
from app.clients.providers.groq_client import GroqClient

from app.config.settings import settings


class AIClientFactory:
    @staticmethod
    def create():

        provider = settings.LLM_PROVIDER.lower()

        logger.info(f"Selected LLM Provider : {provider}")

        if provider == "ollama":
            logger.success(f"Loaded Client : {LlamaClient.__name__}")
            return LlamaClient()

        elif provider == "gemini":
            logger.success(f"Loaded Client : {GeminiClient.__name__}")
            return GeminiClient()

        elif provider == "openai":
            logger.success(f"Loaded Client : {OpenAIClient.__name__}")
            return OpenAIClient()

        if settings.LLM_PROVIDER == "groq":
            logger.success(f"Loaded Client : {GroqClient.__name__}")
            return GroqClient()

        else:
            logger.error(f"Unsupported provider: {provider}")
            raise ValueError(f"Unsupported provider: {provider}")
