from app.services.chat_service import answer_user_message

user_message = "Explain Kubernetes in 3 sentences."

print("qwen2.5 answer:")
print(answer_user_message(user_message))

print("qwen3 answer:")
print(answer_user_message(user_message, model="qwen3:8b"))
