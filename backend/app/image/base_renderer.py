from abc import ABC, abstractmethod


class BaseRenderer(ABC):
    @abstractmethod
    def render(
        self,
        prompt: str,
    ):
        """
        Render an image from a text prompt.
        """
        pass
