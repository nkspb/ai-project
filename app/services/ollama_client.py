import httpx

OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen2.5:7b"
DEFAULT_TIMEOUT = 120.0

def generate_text(
    prompt: str, 
    model: str = DEFAULT_MODEL, 
    timeout: float = DEFAULT_TIMEOUT,
) -> str:
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    r = httpx.post(OLLAMA_GENERATE_URL, json=data, timeout=timeout)
    r.raise_for_status()

    generated_text = r.json()["response"]
    return generated_text