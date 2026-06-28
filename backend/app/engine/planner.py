from app.core.ai_service import AIService
from app.persona.loader import PersonaLoader
from app.strategy.planner_strategy import PlannerStrategy
from app.prompt_builder.builder import PromptBuilder


class Planner:
    def __init__(self):

        self.ai = AIService()

        self.loader = PersonaLoader()

        self.strategy = PlannerStrategy()

        self.prompt_builder = PromptBuilder()

    def generate_plan(self, topic: str):

        strategy = self.strategy.build(topic)

        system_prompt = self.loader.load_prompt("planner")

        prompt = self.prompt_builder.build(
            system_prompt=system_prompt,
            strategy=strategy,
        )

        return self.ai.generate(
            system_prompt=prompt["system_prompt"],
            user_prompt=prompt["user_prompt"],
            temperature=0.3,
        )
