class ContextBuilder:
    def build(self, strategy: dict) -> str:

        return f"""
Topic:
{strategy["topic"]}

Content Pillar:
{strategy["pillar"]}

Content Goal:
{strategy["goal"]}

Tone:
{strategy["tone"]}

Template:
{strategy["template"]}
"""
