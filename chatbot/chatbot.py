import pandas as pd

# Load dataset
df = pd.read_csv("data/financials_analysis.csv")

# Map keywords to dataframe columns & response templates
query_map = {
    "total revenue": {
        "column": "Total Revenue",
        "response": "The total revenue for {company} in {year} was {value:,} million USD."
    },
    "net income margin": {
        "column": "Net Income Margin (%)",
        "response": "The net income margin for {company} in {year} was {value:.2f}%."
    },
    "net income change": {
        "column": "Net Income Growth (%)",
        "response": "For {company}, net income changed by {value:.2f}% in {year} compared to the previous year."
    },
    "debt to assets": {
        "column": "Debt to Assets (%)",
        "response": "In {year}, {company}'s debt-to-assets ratio was {value:.2f}%."
    },
    "cash flow": {
        "column": "Cash Flow From Operating Activities",
        "response": "In {year}, {company}'s cash flow from operating activities was {value:,} million USD."
    }
}


def extract_company_year(user_query: str):
    """Extract company and year from user query."""
    company, year = None, None
    for c in df["Company"].unique():
        if c.lower() in user_query:
            company = c
    for y in df["Year"].unique():
        if str(y) in user_query:
            year = y
    return company, year


def simple_chatbot(user_query: str):
    """Respond to financial queries using predefined mappings."""
    user_query = user_query.lower()

    for keyword, details in query_map.items():
        if keyword in user_query:
            company, year = extract_company_year(user_query)
            if company and year:
                try:
                    value = df.loc[
                        (df["Company"] == company) & (df["Year"] == year),
                        details["column"]
                    ].values[0]
                    return details["response"].format(company=company, year=year, value=value)
                except IndexError:
                    return "Sorry, I couldn’t find data for that request."
            else:
                return "Please include both company and year in your question (e.g., 'Apple 2023')."

    return "Sorry, I can only answer predefined financial queries like revenue, net income, debt-to-assets, etc."
