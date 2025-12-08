import asyncio
import sys

import pykx as kx

from tick_architecture.rdb_schema import quotes
from tick_architecture.rdb_schema import trades


async def main_loop(q, input_trades, input_quotes):
    while True:
        await asyncio.sleep(0.005)
        result = q.poll_recv()
        if result is None:
            continue
        table = result[1]
        if table == 'trades':
            input_trades.upsert(result[2], inplace=True)
        elif table == 'quotes':
            input_quotes.upsert(result[2], inplace=True)

        sys.stdout.write(f"Trades count: {len(input_trades)} Quotes count: {len(input_quotes)}\r")
        sys.stdout.flush()


async def main():
    async with kx.RawQConnection(port=5013) as q:
        await q('.u.sub', '', '')
        await main_loop(q, trades, quotes)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Subscriber suspended')
