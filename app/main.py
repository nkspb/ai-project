from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse
from app.services.chat_service import answer_user_message

from app.services.ollama_client import DEFAULT_MODEL

app = FastAPI(title="AI DevOps Assistant")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    selected_model = request.model or DEFAULT_MODEL

    generated_text = answer_user_message(request.message, request.model)
    return ChatResponse(
        answer=generated_text,
        model=selected_model, 
        backend="ollama",
    )
