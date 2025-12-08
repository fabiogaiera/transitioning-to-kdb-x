import pykx as kx

from intraday_trading_volumes.volumes_histogram_creator import create_histogram

with kx.SyncQConnection(host='localhost', port=5000) as conn:
    print("Connected successfully!")
    taq = conn('select from tv')
    create_histogram(taq.pd())
