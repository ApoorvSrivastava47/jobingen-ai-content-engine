from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4.1")

    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

    DEBUG = os.getenv("DEBUG", "True") == "True"
