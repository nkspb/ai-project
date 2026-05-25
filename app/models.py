from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    message: str = Field(...,min_length=1)
    model: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str
    model: str
    backend: str