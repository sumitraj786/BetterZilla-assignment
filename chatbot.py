import openai

# Set your OpenAI API key here
openai.api_key = "your-api-key"

def ask_chatbot_personalized(question, user_info):
    prompt = f"User Info: {user_info}\n\nQuestion: {question}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Fitness Chatbot: Ask me anything about fitness!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        response = ask_chatbot(user_input)
        print("Chatbot:", response)
