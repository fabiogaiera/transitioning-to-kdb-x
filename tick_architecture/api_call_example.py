from tick_architecture.real_time_processor import rtp

if __name__ == '__main__':
    print(rtp('count_ticks', 'trades', 'AAPL', '2025-01-01', '2020-01-01'))
    print(rtp('count_ticks', 'quotes', 'AAPL', '2025-01-01', '2020-01-01'))
