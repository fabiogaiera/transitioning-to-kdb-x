import sys
import time

import pykx as kx

from tick_architecture.simple_feed_handler.api_client import return_latest_trade_or_quote
from tick_architecture.simple_feed_handler.tickerplant_publisher import publish_to_tickerplant

QUOTES = 'quotes'


def fetch_last_quote(symbol: str):
    quote = return_latest_trade_or_quote(QUOTES, symbol)
    print(quote.text)

    return [kx.TimespanAtom('now'),
            kx.SymbolAtom(symbol),
            kx.FloatAtom(1.0),
            kx.LongAtom(1),
            kx.FloatAtom(1.0),
            kx.LongAtom(1)]


if __name__ == '__main__':
    sym = sys.argv[1]
    try:
        while True:
            last_quote = fetch_last_quote(sym)
            publish_to_tickerplant(QUOTES, last_quote)
            time.sleep(2)
    except KeyboardInterrupt:
        print('Quotes feed handler interrupted.')
