import sys
import time

import pykx as kx

from tick_architecture.simple_feed_handler.api_client import return_latest_trade_or_quote
from tick_architecture.simple_feed_handler.tickerplant_publisher import publish_to_tickerplant

TRADES = 'trades'


def fetch_last_trade(symbol: str):
    trade = return_latest_trade_or_quote(TRADES, symbol)
    print(trade.text)

    return [kx.TimespanAtom('now'),
            kx.SymbolAtom(symbol),
            kx.FloatAtom(1.0),
            kx.LongAtom(1)]


if __name__ == '__main__':
    sym = sys.argv[1]
    try:
        while True:
            last_trade = fetch_last_trade(sym)
            publish_to_tickerplant(TRADES, last_trade)
            time.sleep(2)
    except KeyboardInterrupt:
        print('Trades feed handler interrupted.')
