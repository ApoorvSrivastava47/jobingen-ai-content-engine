from app.agents.base_agent import BaseAgent


class Copywriter(BaseAgent):
    def __init__(self):

        super().__init__()

    def write(
        self,
        strategy: dict,
        platform: str = "linkedin",
        previous_content: str = None,
        feedback: str = None,
    ):

        system_prompt = self.loader.load_prompt(
            "copywriter",
        )

        context = strategy.copy()

        context["platform"] = platform

        if previous_content:
            context["previous_content"] = previous_content

        if feedback:
            context["reviewer_feedback"] = feedback

        prompt = self.prompt_builder.build(
            system_prompt=system_prompt,
            context=context,
        )

        return self.ai.generate(
            system_prompt=prompt["system_prompt"],
            user_prompt=prompt["user_prompt"],
            temperature=0.7,
        )
