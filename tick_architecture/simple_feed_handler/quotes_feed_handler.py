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

QUOTES = 'quotes'


# Returns a list composed as follows: [Time, Symbol, Ask Price, Ask Size, Bid Price, Bid Size]
def create_list_of_values(symbol: str):
    values = return_latest_trade_or_quote(QUOTES, symbol)
    ask_price = values['ap']
    ask_size = values['as']
    bid_price = values['bp']
    bid_size = values['bs']
    time_span = convert_to_time_span(values['t'])
    return [kx.q(time_span),
            kx.SymbolAtom(symbol),
            kx.FloatAtom(ask_price),
            kx.LongAtom(ask_size),
            kx.FloatAtom(bid_price),
            kx.LongAtom(bid_size)]


if __name__ == '__main__':
    sym = sys.argv[1]
    try:
        last_time = None
        while True:
            last_quote = create_list_of_values(sym)
            # Comparison between two quotes based on their timestamp to determine whether to send or not quote to the tickerplant
            if (last_time != last_quote[0]) or last_time is None:
                publish_to_tickerplant(QUOTES, last_quote)
                logging.info(
                    f"Time: {last_quote[0]} | Symbol: {last_quote[1]} | Ask Price: {last_quote[2]} | Ask Size: {last_quote[3]} | Bid Price: {last_quote[4]} | Bid Size: {last_quote[5]}"
                )
            last_time = last_quote[0]
            time.sleep(2)
    except KeyboardInterrupt:
        print('Quotes feed handler interrupted.')
