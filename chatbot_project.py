# Simple chatbot using only Python

print("Hello! I'm your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "i feel low":
        print("Bot: It's okay to feel low. Take some rest or talk to a friend.")
    elif user_input == "i am happy":
        print("Bot: Yay! I'm happy to hear that 😊")
    elif user_input == "i am sad":
        print("Bot: It's alright to feel sad sometimes. I'm here for you.")
    elif user_input == "what should i do?":
        print("Bot: You can talk to someone, take a break, or go for a walk.")
    elif user_input == "bye":
        print("Bot: Bye! Take care 💖")
        break
    else:
        print("Bot: I'm not sure how to respond. Can you say it differently?")