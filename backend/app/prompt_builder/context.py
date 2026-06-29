class ContextBuilder:
    def build(
        self,
        context: dict,
    ) -> str:

        lines = []

        for key, value in context.items():
            title = key.replace("_", " ").title()

            lines.append(f"{title}:\n{value}")

        return "\n\n".join(lines)
