import pykx as kx


def custom_api(table, symbol):
    return kx.q(f'select from {table} where sym = `{symbol}')
