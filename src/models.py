from pydantic import BaseModel
from typing import List

class Query(BaseModel):
    query: str

class Response(BaseModel):
    response: str
    context: List[str]