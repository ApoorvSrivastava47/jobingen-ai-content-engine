from google import genai

from app.config.settings import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Reply with exactly: Hello Raman",
)

print(response.text)
