from pydantic import BaseModel


class GenerateRequest(BaseModel):
    topic: str
