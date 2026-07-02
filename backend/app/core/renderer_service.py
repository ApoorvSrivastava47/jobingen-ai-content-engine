from pathlib import Path

from app.clients.renderer_factory import RendererFactory
from app.config.settings import settings


class RendererService:
    def __init__(self):

        self.renderer = RendererFactory.create()

        settings.IMAGE_OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def render(
        self,
        prompt: str,
        filename: str = "generated.png",
    ):

        image = self.renderer.render(prompt)

        output_path = settings.IMAGE_OUTPUT_DIR / filename

        with open(output_path, "wb") as file:
            file.write(image)

        return str(output_path)
