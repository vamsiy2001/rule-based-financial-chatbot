import pytest
from chatbot.chatbot import simple_chatbot

def test_revenue_query():
    response = simple_chatbot("What is the total revenue of Apple 2023?")
    assert "Apple" in response
    assert "2023" in response
    assert "revenue" in response.lower()

def test_invalid_query():
    response = simple_chatbot("Tell me about dividends")
    assert "Sorry" in response
