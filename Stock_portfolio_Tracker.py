# Rule-Based Chatbot in Python

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for consistency

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I am RuleBot, your simple chatbot."
    elif "help" in user_input:
        return "Sure! I can answer basic questions like greetings, name, and well-being."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that. Try asking something else."

# Chat loop
print("ChatBot: Hello! I am RuleBot. Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBot:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
