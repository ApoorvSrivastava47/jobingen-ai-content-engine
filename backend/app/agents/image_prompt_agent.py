from app.agents.base_agent import BaseAgent


class ImagePromptAgent(BaseAgent):
    SYSTEM_PROMPT = """
You are an expert Creative Director.

Your job is to convert business content into
high-quality AI image prompts.

Always produce prompts that are:

- Professional
- Modern
- Corporate
- Minimal
- Blue and white color palette
- No text inside the image
- Premium quality

Return ONLY the final image prompt.
"""

    def __init__(self):

        super().__init__()

    def generate(
        self,
        strategy: dict,
        content: str,
        platform: str = "linkedin",
    ):

        user_prompt = f"""
Platform:
{platform}

Strategy:
{strategy}

Content:
{content}

Generate a professional AI image prompt suitable for {platform}.
"""

        return self.ai.generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=user_prompt,
            temperature=0.7,
        )
