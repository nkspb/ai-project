from app.services.ollama_client import generate_text

def build_prompt(user_message: str) -> str:
    prompt = f"""
    You are an assistant helping a DevOps engineer. 
    Answer clearly and practically.
    User question: {user_message}
    """
    return prompt.strip()


user_message = "Explain Kubernetes in 3 sentences."
prompt = build_prompt(user_message)

print("qwen2.5 answer:")
print(generate_text(prompt))

print("qwen3 answer:")
print(generate_text(prompt, model="qwen3:8b"))

