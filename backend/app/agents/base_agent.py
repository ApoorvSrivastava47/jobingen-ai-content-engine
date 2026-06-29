from app.core.ai_service import AIService
from app.persona.loader import PersonaLoader
from app.prompt_builder.builder import PromptBuilder


class BaseAgent:
    def __init__(self):

        self.ai = AIService()

        self.loader = PersonaLoader()

        self.prompt_builder = PromptBuilder()
