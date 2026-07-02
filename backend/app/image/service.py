from app.image.factory import ImageFactory

from app.config.settings import settings


class ImageService:
    def __init__(self):

        self.renderer = ImageFactory.create()

        settings.IMAGE_OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        prompt: str,
        filename: str,
    ):

        image = self.renderer.render(
            prompt,
        )

        output = settings.IMAGE_OUTPUT_DIR / filename

        image.save(output)

        # Return only filename
        return filename
