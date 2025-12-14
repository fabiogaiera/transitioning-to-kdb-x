import pykx as kx


def publish_to_tickerplant(table, message):
    with kx.SyncQConnection(host='localhost', port=5010, wait=False) as q:
        q('.u.upd', table, message)
