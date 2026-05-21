import httpx

llm_api = "http://localhost:11434/api/generate"
llm_model = "qwen2.5:7b"

data = {
    "model": llm_model, 
    "prompt": "Hello! How are you?", 
    "stream": False,
}

r = httpx.post(llm_api, json=data)
print(f"HTTP Status: {r.status_code}")
r.raise_for_status() # Check this response

response_data = r.json()

def generate_text(prompt: str) -> str:
    r = httpx.post(llm_api, json=data)
    r.raise_for_status()
    return r.json()

print(generate_text("Hello mate!"))
# print(f"Raw JSON response: {response_data}")
# print(f"response field: {response_data['response']}")