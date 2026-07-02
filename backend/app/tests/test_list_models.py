from google import genai

from app.config.settings import settings


def main():

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY,
    )

    print("\nAvailable Models\n")

    for model in client.models.list():
        print(model.name)


if __name__ == "__main__":
    main()
