from app.strategy.planner_strategy import PlannerStrategy


class PlannerAgent:
    def __init__(self):

        self.strategy = PlannerStrategy()

    def plan(
        self,
        topic: str,
        platform: str = "linkedin",
    ):

        strategy = self.strategy.build(topic)

        strategy["platform"] = platform

        return strategy
