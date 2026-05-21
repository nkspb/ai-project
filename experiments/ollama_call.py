import httpx

llm_api = "http://localhost:11434/api/generate"
llm_model = "qwen2.5:7b"

def generate_text(prompt: str) -> str:
    data = {
        "model": llm_model,
        "prompt": prompt,
        "stream": False

    }
    r = httpx.post(llm_api, json=data)
    r.raise_for_status()
    generated_text = r.json()["response"]

    return generated_text

def build_prompt(user_message: str) -> str:
    prompt = f"""
    You are an assistant helping a DevOps engineer. 
    Answer clearly and practically.
    User question: {user_message}
    """
    return prompt.strip()


user_message = "Explain Kubernetes in 3 sentences."
prompt = build_prompt(user_message)
answer = generate_text(prompt)

print(answer)