from app.config.settings import settings

from app.image.huggingface_renderer import HuggingFaceRenderer


class ImageFactory:
    @staticmethod
    def create():

        provider = settings.IMAGE_PROVIDER.lower()

        if provider == "huggingface":
            return HuggingFaceRenderer()

        raise ValueError(f"Unsupported Image Provider : {provider}")
