from app.critic.score import QUALITY_SCORE


class ContentEvaluator:
    def evaluate(self, content: str):

        report = {}

        for category, max_score in QUALITY_SCORE.items():
            report[category] = {
                "score": max_score,
                "max_score": max_score,
            }

        report["total"] = sum(QUALITY_SCORE.values())

        report["recommendation"] = "publish"

        return report
