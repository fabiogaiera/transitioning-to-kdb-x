import pykx as kx


def preprocessor(table, data):
    if table == 'trade':
        return data
    else:
        return None


def postprocessor(table, data):
    agg = kx.q[table].select(
        columns={'min_px': 'min price',
                 'max_px': 'max price',
                 'spread_px': 'max[price] - min price'},
        by={'symbol': 'symbol'})
    kx.q['agg'] = agg  # Make the table accessible from q
    with kx.SyncQConnection(port=5010, wait=False, no_ctx=True) as q:
        q('.u.upd', 'aggregate', agg._values)
    return None


rtp = kx.tick.RTP(port=5014,
                  subscriptions=['trades'],
                  libraries={'kx': 'pykx'},
                  pre_processor=preprocessor,
                  post_processor=postprocessor,
                  vanilla=False)

if __name__ == '__main__':
    rtp.start({'tickerplant': 'localhost:5013'})
