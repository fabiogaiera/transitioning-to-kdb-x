import logging
import sys
import time

import pykx as kx

from tick_architecture.simple_feed_handler.api_client import return_latest_trade_or_quote
from tick_architecture.simple_feed_handler.tickerplant_publisher import publish_to_tickerplant
from tick_architecture.simple_feed_handler.utils import convert_to_time_span

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

TRADES = 'trades'


# Returns a list composed as follows [Time, Symbol, Price, Size]
def create_list_of_values(symbol: str):
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
        last_time = None
        while True:
            last_trade = create_list_of_values(sym)
            # Comparison between two trades based on their timestamp to determine whether to send or not trade to the tickerplant
            if (last_time != last_trade[0]) or last_time is None:
                publish_to_tickerplant(TRADES, last_trade)
                logging.info(
                    f"Time: {last_trade[0]} | Symbol: {last_trade[1]} | Price: {last_trade[2]} | Size: {last_trade[3]}"
                )
            last_time = last_trade[0]
            time.sleep(2)
    except KeyboardInterrupt:
        print('Trades feed handler interrupted.')
