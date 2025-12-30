from transformers import pipeline

# Load text generation model
chatbot = pipeline(
    "text-generation",
    model="gpt2",
    device=-1  # CPU
)

print("🤖 AI Chatbot: Type 'quit' to exit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bot: Goodbye 👋")
        break

    response = chatbot(
        user_input,
        max_new_tokens=50,
        temperature=0.7,
        top_p=0.9,
        num_return_sequences=1
    )

    reply = response[0]["generated_text"]
    print("Bot:", reply)
