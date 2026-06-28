from abc import ABC, abstractmethod


class BaseAIClient(ABC):
    """
    Base interface for every AI Provider.

    Every provider (OpenAI, Gemini, Claude)
    must implement this contract.
    """

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:
        """
        Generate text from an AI provider.
        """
        pass
