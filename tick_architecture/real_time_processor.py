import pykx as kx

import tick_architecture.api

rtp = kx.tick.RTP(port=5014,
                  subscriptions=['trades', 'quotes'],
                  libraries={'kx': 'pykx'},
                  vanilla=False)

if __name__ == '__main__':
    rtp.start({'tickerplant': 'localhost:5013'})
    rtp.register_api('select_query', tick_architecture.api.custom_api)
