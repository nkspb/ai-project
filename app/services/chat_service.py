from app.services.ollama_client import generate_text, DEFAULT_MODEL

def answer_user_message(user_message: str, model: str | None = None) -> str:
    prompt = _build_prompt(user_message)
    selected_model = model or DEFAULT_MODEL
    generated_text = generate_text(prompt, model=selected_model)
    print(f"Selected model: {selected_model}")
    return generated_text

def _build_prompt(user_message: str) -> str:
    prompt = f"""
    You are an assistant helping a DevOps engineer. 
    Answer clearly and practically.

    User question: 
    {user_message}
    """
    return prompt.strip()