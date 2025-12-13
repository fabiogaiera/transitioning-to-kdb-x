import time

import pykx as kx


def fetch_trades():
    while True:
        time.sleep(4)
        with kx.SyncQConnection(host='localhost', port=5010, wait=False) as q:
            msg_trades = [kx.TimespanAtom('now'),
                          kx.SymbolAtom('AAPL'),
                          kx.FloatAtom(1.0),
                          kx.LongAtom(1)]
            q('.u.upd', 'trades', msg_trades)


if __name__ == '__main__':
    fetch_trades()
