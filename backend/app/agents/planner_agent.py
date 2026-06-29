from app.strategy.planner_strategy import PlannerStrategy


class PlannerAgent:
    def __init__(self):

        self.strategy = PlannerStrategy()

    def plan(
        self,
        topic: str,
    ):

        return self.strategy.build(topic)
