import sys
import time

import pykx as kx

from tick_architecture.simple_feed_handler.api_client import return_latest_trade_or_quote
from tick_architecture.simple_feed_handler.tickerplant_publisher import publish_to_tickerplant
from tick_architecture.simple_feed_handler.utils import convert_to_time_span

TRADES = 'trades'


def fetch_last_trade(symbol: str):
    values = return_latest_trade_or_quote(TRADES, symbol)
    price = values['p']
    size = values['s']
    time_span = convert_to_time_span(values['t'])
    return [kx.q(time_span),
            kx.SymbolAtom(symbol),
            kx.FloatAtom(price),
            kx.LongAtom(size)]


if __name__ == '__main__':
    sym = sys.argv[1]
    try:
        while True:
            last_trade = fetch_last_trade(sym)
            publish_to_tickerplant(TRADES, last_trade)
            time.sleep(2)
    except KeyboardInterrupt:
        print('Trades feed handler interrupted.')
