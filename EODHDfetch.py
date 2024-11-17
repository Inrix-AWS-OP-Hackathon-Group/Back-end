import requests
import json




with open("exchangeSymbols.json", 'r') as file:
    exchangeSymbols = json.load(file)


tickers = []

for i in exchangeSymbols:
    if (i["isin"] is not None and i["Type"] is "Common Stock"):
        tickers.append(i["Code"])

def callEODHD():
    for i in tickers:

        params = {
            "s": i + ".US",
        }

        try:
            response = requests.get(API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            print("API fetch succeeded")

            with open("financialNews.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Data saved successfully")
        except requests.exceptions.RequestException as err:
            print(f"An error was encountered while fetching data: {err}")

callEODHD()
