import requests

# Step 1: Function to fetch data from EODHD and aggreagate into a single object for a ticker
# Data includes: Sentiment Analysis

def fetch_eodhd(ticker):
    url = f'https://eodhd.com/api/sentiments?s={ticker.lower()}.us&from=2024-11-10&to=2024-11-15&api_token=62a4b058a96d71.91558808&fmt=json'
    response = requests.get(url)
    curr_str = f'{ticker.upper()}.US'
    data = response.json()[curr_str]

    vals = []

    for i in data:
        vals.append(i['normalized'])

    sentiment = (sum(vals) / len(vals))
    return sentiment



# Step 2: Function to fetch data from S3 Bucket and send it to Bedrock
# Bedrock be prompted twice, once to give a rating
# second to give a general summary of risk factors for a company





# Tests
# fetch_eodhd('AAPL')

