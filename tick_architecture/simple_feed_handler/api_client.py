import os

import requests

headers = {

    "accept": "application/json",
    "APCA-API-KEY-ID": os.getenv("API_KEY"),
    "APCA-API-SECRET-KEY": os.getenv("API_SECRET")

}

url_trades = "https://data.alpaca.markets/v2/stocks/trades/latest?symbols=AAPL"
url_quotes = "https://data.alpaca.markets/v2/stocks/quotes/latest?symbols=AAPL"

response1 = requests.get(url_trades, headers=headers)
response2 = requests.get(url_quotes, headers=headers)

print(response1.text)
print(response2.text)
