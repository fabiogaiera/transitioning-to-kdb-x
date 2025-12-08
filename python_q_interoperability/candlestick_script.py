import pykx as kx

from candlestick_chart.candlestick_chart_creator import create_candlestick_chart

with kx.SyncQConnection(host='localhost', port=5001) as conn:
    print("Connected successfully!")
    taq = conn('select from ohlcv')
    create_candlestick_chart(taq.pd())
