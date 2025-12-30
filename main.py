from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

print("🤖 AI Chatbot: Type 'quit' to exit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    print("Bot:", response[0]["generated_text"])


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

