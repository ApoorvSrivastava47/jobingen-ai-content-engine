from app.image.gemini_image_client import GeminiImageClient


def main():

    client = GeminiImageClient()

    prompt = """
A futuristic AI powered hospital,
clean modern design,
blue lighting,
professional illustration.
"""

    print("=" * 60)
    print("Generating Image...")
    print("=" * 60)

    response = client.generate(prompt)

    print(response)


if __name__ == "__main__":
    main()
