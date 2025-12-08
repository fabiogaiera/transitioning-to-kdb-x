import pykx as kx

from bid_ask_spread.bid_ask_spread_chart_creator import create_chart

with kx.SyncQConnection(host='localhost', port=5002) as conn:
    print("Connected successfully!")
    bid_ask_spread = conn('select from bas')
    create_chart(bid_ask_spread.pd())
