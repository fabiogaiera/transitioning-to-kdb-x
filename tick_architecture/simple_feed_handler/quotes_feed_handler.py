import pykx as kx
import sys
import time

from tick_architecture.simple_feed_handler.api_client import return_latest_trade_or_quote
from tick_architecture.simple_feed_handler.tickerplant_publisher import publish_to_tickerplant
from tick_architecture.simple_feed_handler.utils import convert_to_time_span

QUOTES = 'quotes'


# Returns a list containing Time, Symbol, Ask Price, Ask Size, Bid Price, Bid Size
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
        while True:
            last_quote = create_list_of_values(sym)
            publish_to_tickerplant(QUOTES, last_quote)
            time.sleep(2)
    except KeyboardInterrupt:
        print('Quotes feed handler interrupted.')
