from app.agents.base_agent import BaseAgent


class CriticAgent(BaseAgent):
    def __init__(self):

        super().__init__()

    def review(
        self,
        content: str,
        platform: str = "linkedin",
    ):

        system_prompt = self.loader.load_prompt(
            "critic",
        )

        prompt = self.prompt_builder.build(
            system_prompt=system_prompt,
            context={
                "content": content,
                "platform": platform,
            },
        )

        return self.ai.generate(
            system_prompt=prompt["system_prompt"],
            user_prompt=prompt["user_prompt"],
            temperature=0.0,
        )
