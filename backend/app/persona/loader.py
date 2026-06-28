from pathlib import Path
import yaml


class PersonaLoader:
    """
    Loads the active Gen persona prompts from the prompts directory.
    """

    def __init__(self):
        self.base_path = Path(__file__).resolve().parents[2] / "prompts" / "persona"

        version_file = self.base_path / "versions.yaml"

        with open(version_file, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        self.active_version = config["active_version"]

    def load_prompt(self, mode: str) -> str:
        """
        mode:
            planner
            copywriter
            critic
        """

        prompt_path = self.base_path / self.active_version / f"{mode}.md"

        if not prompt_path.exists():
            raise FileNotFoundError(f"{mode}.md not found inside {self.active_version}")

        with open(prompt_path, "r", encoding="utf-8") as file:
            return file.read()
