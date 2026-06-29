from pprint import pprint

from app.workflow.content_workflow import ContentWorkflow

workflow = ContentWorkflow()

result = workflow.execute("AI Resume Building Tips")

print()

print("=" * 60)
print("CONTENT WORKFLOW")
print("=" * 60)

pprint(result)
