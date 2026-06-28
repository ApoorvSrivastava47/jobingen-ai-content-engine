from pathlib import Path
from loguru import logger
import yaml


class PersonaValidator:
    def __init__(self):
        self.base_path = Path("prompts/persona")

    def validate(self):
        versions_file = self.base_path / "versions.yaml"

        if not versions_file.exists():
            raise FileNotFoundError("versions.yaml not found.")

        versions = yaml.safe_load(versions_file.read_text(encoding="utf-8"))

        active_version = versions.get("active_version")

        if not active_version:
            raise ValueError("active_version missing.")

        version_path = self.base_path / active_version

        if not version_path.exists():
            raise FileNotFoundError(f"Version folder '{active_version}' not found.")

        required_prompts = [
            "planner.md",
            "copywriter.md",
            "critic.md",
        ]

        for prompt in required_prompts:
            prompt_file = version_path / prompt

            if not prompt_file.exists():
                raise FileNotFoundError(f"{prompt} missing.")

            content = prompt_file.read_text(encoding="utf-8").strip()

            if not content:
                raise ValueError(f"{prompt} is empty.")

            logger.info(f"Validated : {prompt}")

        logger.success("Persona validation completed successfully.")
