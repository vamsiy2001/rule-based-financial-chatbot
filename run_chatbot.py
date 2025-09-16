from chatbot.chatbot import simple_chatbot

if __name__ == "__main__":
    print("👋 Hi! I’m your Financial Chatbot.")
    print("Ask me about revenue, net income margin, cash flow, or debt-to-assets for Microsoft, Tesla, or Apple (2022–2024).")
    print("Type 'exit' or 'quit' anytime to stop.\n")

    while True:
        query = input("You: ")
        if query.lower() in ["quit", "exit"]:
            print("Bot: Goodbye 👋 Have a great day!")
            break
        print("Bot:", simple_chatbot(query))
