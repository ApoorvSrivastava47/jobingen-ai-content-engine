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
        context: dict,
    ):

        context_text = self.context.build(context)

        instructions = self.instructions.build()

        user_prompt = self.formatter.format(
            context=context_text,
            instructions=instructions,
        )

        return {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
        }
