import pykx as kx


# Count ticks for a given table, symbol, start_time and end_time
def count_ticks(table, symbol, start_time, end_time):
    return kx.q(f'select count i from {table} where time within ({start_time};{end_time}), sym = `{symbol}')
