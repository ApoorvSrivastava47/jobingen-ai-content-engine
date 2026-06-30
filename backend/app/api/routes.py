from fastapi import APIRouter

from app.schemas.request import GenerateRequest
from app.workflow.content_workflow import ContentWorkflow

router = APIRouter()

workflow = ContentWorkflow()


@router.post("/generate")
def generate(request: GenerateRequest):

    result = workflow.execute(request.topic)

    return result
