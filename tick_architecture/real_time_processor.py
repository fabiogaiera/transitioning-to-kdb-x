import pykx as kx


def custom_api(table, symbol):
    return kx.q(f'select from {table} where sym = `{symbol}')


rtp = kx.tick.RTP(port=5014,
                  subscriptions=['trades', 'quotes'],
                  libraries={'kx': 'pykx'},
                  apis={'select_query': custom_api},
                  vanilla=False)

if __name__ == '__main__':
    rtp.start({'tickerplant': 'localhost:5013'})
