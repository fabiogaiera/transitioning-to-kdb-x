import os

import requests

headers = {

    "accept": "application/json",
    "APCA-API-KEY-ID": os.getenv("API_KEY"),
    "APCA-API-SECRET-KEY": os.getenv("API_SECRET")

}


def return_latest_trade_or_quote(trade_quote, symbol):
    url = f"https://data.alpaca.markets/v2/stocks/{trade_quote}/latest?symbols={symbol}"
    return requests.get(url, headers=headers)
