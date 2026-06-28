from app.core.ai_service import AIService
from app.persona.loader import PersonaLoader


class Planner:
    def __init__(self):
        self.ai = AIService()
        self.loader = PersonaLoader()

    def generate_plan(self, topic: str):

        system_prompt = self.loader.load_prompt("planner")

        user_prompt = f"""
Create a social media content plan for:

Topic:
{topic}
"""

        return self.ai.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.3,
        )
