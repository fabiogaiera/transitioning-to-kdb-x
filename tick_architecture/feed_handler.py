import time

import pykx as kx

while True:
    time.sleep(4)
    with kx.SyncQConnection(host='localhost', port=5010, wait=False) as q:
        msgTrades = [kx.TimespanAtom('now'),
                     kx.SymbolAtom('AAPL'),
                     kx.FloatAtom(1.0),
                     kx.LongAtom(1)]
        msgQuotes = [kx.TimespanAtom('now'),
                     kx.SymbolAtom('AAPL'),
                     kx.FloatAtom(1.0),
                     kx.LongAtom(1),
                     kx.FloatAtom(1.0),
                     kx.LongAtom(1)]
        q('.u.upd', 'trades', msgTrades)
        q('.u.upd', 'quotes', msgQuotes)
