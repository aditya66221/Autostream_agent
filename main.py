from agent import Agent

def run_chat():
    bot = Agent()

    print("🚀 AutoStream AI Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = bot.handle_input(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    run_chat()