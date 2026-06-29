from app.agents.planner_agent import PlannerAgent
from app.agents.copywriter_agent import Copywriter
from app.agents.critic_agent import CriticAgent
from app.utils.review_parser import ReviewParser


class ContentWorkflow:
    def __init__(self):

        self.planner = PlannerAgent()

        self.copywriter = Copywriter()

        self.critic = CriticAgent()

        self.review_parser = ReviewParser()

        self.max_revisions = 2

    def execute(
        self,
        topic: str,
    ):

        strategy = self.planner.plan(topic)

        content = self.copywriter.write(strategy)

        attempts = 0

        while True:
            review = self.critic.review(content)

            if not self.review_parser.should_rewrite(review):
                break

            if attempts >= self.max_revisions:
                break

            print(f"\n🔄 Revision Attempt {attempts + 1}\n")

            content = self.copywriter.write(
                strategy=strategy,
                previous_content=content,
                feedback=review,
            )

            attempts += 1

        return {
            "strategy": strategy,
            "content": content,
            "review": review,
        }
