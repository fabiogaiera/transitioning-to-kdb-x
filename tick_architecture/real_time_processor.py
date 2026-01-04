import pykx as kx

from tick_architecture.api import count_ticks

rtp = kx.tick.RTP(port=5014,
                  subscriptions=['trades', 'quotes'],
                  libraries={'kx': 'pykx'},
                  vanilla=False)

if __name__ == '__main__':
    rtp.start({'tickerplant': 'localhost:5013'})
    rtp.register_api('count_ticks', count_ticks)
