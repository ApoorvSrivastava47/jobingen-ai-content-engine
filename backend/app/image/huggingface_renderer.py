from huggingface_hub import InferenceClient

from app.config.settings import settings

from app.image.base_renderer import BaseRenderer


class HuggingFaceRenderer(BaseRenderer):
    def __init__(self):

        self.client = InferenceClient(
            provider="hf-inference",
            api_key=settings.HF_API_KEY,
        )

        self.model = settings.HF_MODEL

    def render(
        self,
        prompt: str,
    ):

        image = self.client.text_to_image(
            prompt=prompt,
            model=self.model,
        )

        return image
