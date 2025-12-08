import pykx as kx

trades = kx.schema.builder({
    'time': kx.TimespanAtom,
    'sym': kx.SymbolAtom,
    'price': kx.FloatAtom,
    'size': kx.LongAtom})

quotes = kx.schema.builder({
    'time': kx.TimespanAtom,
    'sym': kx.SymbolAtom,
    'ask_price': kx.FloatAtom,
    'ask_size': kx.LongAtom,
    'bid_price': kx.FloatAtom,
    'bid_size': kx.LongAtom})
