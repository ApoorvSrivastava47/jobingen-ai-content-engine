from pathlib import Path


class Settings:
    PROJECT_ROOT = Path.cwd()

    PROMPTS_DIR = PROJECT_ROOT / "prompts"

    OUTPUT_DIR = PROJECT_ROOT / "outputs"

    LOG_DIR = PROJECT_ROOT / "logs"

    DATA_DIR = PROJECT_ROOT / "data"
