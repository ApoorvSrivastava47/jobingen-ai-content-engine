from app.config.settings import settings

from app.renderer.huggingface_renderer import HuggingFaceRenderer
from app.renderer.gemini_renderer import GeminiRenderer


class RendererFactory:
    @staticmethod
    def create():

        provider = settings.IMAGE_PROVIDER.lower()

        if provider == "huggingface":
            return HuggingFaceRenderer()

        elif provider == "gemini":
            return GeminiRenderer()

        else:
            raise ValueError(f"Unsupported image provider : {provider}")
