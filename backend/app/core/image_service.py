from app.clients.image_factory import ImageClientFactory


class ImageService:
    def __init__(self):

        self.client = ImageClientFactory.create()

    def generate_image(
        self,
        prompt: str,
    ):

        return self.client.generate(prompt)
