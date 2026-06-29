from app.agents.planner_agent import PlannerAgent
from app.agents.copywriter_agent import Copywriter


class Planner:
    def __init__(self):

        self.planner = PlannerAgent()

        self.copywriter = Copywriter()

    def generate_plan(
        self,
        topic: str,
    ):

        strategy = self.planner.plan(topic)

        return self.copywriter.write(strategy)
