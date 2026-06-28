from app.prompt_builder.context import ContextBuilder
from app.prompt_builder.instructions import InstructionBuilder
from app.prompt_builder.formatter import PromptFormatter


class PromptBuilder:
    def __init__(self):

        self.context = ContextBuilder()

        self.instructions = InstructionBuilder()

        self.formatter = PromptFormatter()

    def build(
        self,
        system_prompt: str,
        strategy: dict,
    ):

        context = self.context.build(strategy)

        instructions = self.instructions.build()

        user_prompt = self.formatter.format(
            context=context,
            instructions=instructions,
        )

        return {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
        }
