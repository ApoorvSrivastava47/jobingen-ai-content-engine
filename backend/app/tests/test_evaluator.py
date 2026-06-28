from pprint import pprint

from app.critic.evaluator import ContentEvaluator


evaluator = ContentEvaluator()

report = evaluator.evaluate("Dummy Content")

print()

print("=" * 60)

print("EVALUATION REPORT")

print("=" * 60)

pprint(report)
