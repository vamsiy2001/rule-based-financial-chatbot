# Financial Chatbot 🤖

This is a simple **rule-based chatbot** that answers financial queries (like revenue, net income, debt-to-assets) for Microsoft, Tesla, and Apple using data from SEC 10-K/10-Q filings.

## Features
- Ask about Total Revenue, Net Income Margin, Debt-to-Assets, Cash Flow, and Growth %.
- Works for multiple years (2021–2023).
- Runs in the terminal with a friendly chatbot interface.

## Project Structure
```
financial-chatbot/
│── chatbot/              # Chatbot logic (Python scripts)
│── data/                 # Financial dataset (CSV from SEC filings)
│── tests/                # Basic test cases
│── run_chatbot.py        # Entry point to run chatbot
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
│── .gitignore
```

## Installation & Usage
```bash
# Clone repo
git clone https://github.com/<your-username>/financial-chatbot.git
cd financial-chatbot

# Install dependencies
pip install -r requirements.txt

# Run chatbot
python run_chatbot.py
```

## Example Interaction
```
👋 Hi! I’m your Financial Chatbot.
Ask me about revenue, net income margin, cash flow, or debt-to-assets.
Type 'exit' or 'quit' anytime to stop.

You: What was Apple total revenue in 2023?
Bot: The total revenue for Apple in 2023 was 383,285 million USD.
```

## Limitations
- Only supports predefined queries (not NLP).
- Limited to Apple, Microsoft, Tesla (2021–2023).
- Not a real AI model, but a **rule-based demo chatbot**.

---
📌 Good starting point for financial data projects and chatbot prototypes.
