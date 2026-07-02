import requests

from app.config.settings import settings


class HuggingFaceRenderer:
    def __init__(self):

        self.api_url = (
            f"https://api-inference.huggingface.co/models/{settings.HF_MODEL}"
        )

        self.headers = {"Authorization": f"Bearer {settings.HF_API_KEY}"}

    def render(
        self,
        prompt: str,
    ):

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={"inputs": prompt},
            timeout=300,
        )

        response.raise_for_status()

        return response.content
