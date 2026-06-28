from app.strategy.rules import get_strategy


class PlannerStrategy:
    def build(self, topic: str):

        return get_strategy(topic)
