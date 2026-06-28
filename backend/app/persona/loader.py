from pathlib import Path
import yaml
from loguru import logger


class PersonaLoader:
    def __init__(self):
        self.base_path = Path("prompts/persona")

        versions = yaml.safe_load(
            (self.base_path / "versions.yaml").read_text(encoding="utf-8")
        )

        self.active_version = versions["active_version"]

        logger.info(f"Loaded Persona Version : {self.active_version}")

    def load_prompt(self, prompt_name: str) -> str:
        prompt_path = self.base_path / self.active_version / f"{prompt_name}.md"

        logger.info(f"Loading Prompt : {prompt_name}")

        return prompt_path.read_text(encoding="utf-8")
