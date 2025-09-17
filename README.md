# Financial Chatbot 🤖

# Rule-Based Financial Chatbot 🤖

This repository contains a **rule-based financial chatbot** developed as part of the  
**Forage BCGX GenAI Virtual Experience Program**.  

The chatbot answers financial queries (like **revenue, net income, debt-to-assets ratio**) for  
**Microsoft, Tesla, and Apple** using structured data extracted from SEC **10-K/10-Q filings**.

---

## 📌 Learning Outcomes

This project provided practical hands-on experience in:  
- 📊 Extracting and structuring financial data from **real-world SEC filings**  
- 🤖 Developing a **lightweight rule-based chatbot**  
- 🗂️ Organizing code, datasets, and documentation for reproducibility  

While this is **not an advanced AI/LLM chatbot**, it demonstrates how financial data can be  
transformed into **interactive query systems**, serving as a starting point for more advanced projects.  

---

## 🚀 Features
- Ask about **Total Revenue, Net Income Margin, Debt-to-Assets, Cash Flow, and Growth %**  
- Supports queries across **multiple years (2021–2023)**  
- Runs in the **terminal with a chatbot-style interface**  
- Beginner-friendly, reproducible, and extendable  

---
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

## ⚙️ Installation & Usage
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
