import pykx as kx

with kx.SyncQConnection(port=5014, no_ctx=True) as q:
    print(q('count trades'))
