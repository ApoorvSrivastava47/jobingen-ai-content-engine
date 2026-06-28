class PromptFormatter:
    def format(
        self,
        context: str,
        instructions: str,
    ) -> str:

        return f"""
{context}

{instructions}
"""
