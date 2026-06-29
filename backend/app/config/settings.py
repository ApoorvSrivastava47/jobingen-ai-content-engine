from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_ROOT = Path.cwd()

    PROMPTS_DIR = PROJECT_ROOT / "prompts"

    OUTPUT_DIR = PROJECT_ROOT / "outputs"

    LOG_DIR = PROJECT_ROOT / "logs"

    DATA_DIR = PROJECT_ROOT / "data"

    # -------------------------
    # LLM Provider
    # -------------------------

    LLM_PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "ollama",
    )

    # -------------------------
    # Ollama
    # -------------------------

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2",
    )

    # -------------------------
    # Gemini
    # -------------------------

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY",
    )

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash",
    )

    # -------------------------
    # OpenAI
    # -------------------------

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
    )

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-4.1",
    )


settings = Settings()
