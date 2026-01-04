from tick_architecture.real_time_processor_starter import rtp

if __name__ == '__main__':
    print(rtp('count_ticks', 'trades', 'AAPL', '13:30:00.000000000', '22:00:00.000000000'))
    print(rtp('count_ticks', 'quotes', 'AAPL', '13:30:00.000000000', '22:00:00.000000000'))
    print(rtp('count_ticks', 'trades', 'AAPL', '13:30:00.000000000', '14:00:00.000000000'))
    print(rtp('count_ticks', 'quotes', 'AAPL', '13:30:00.000000000', '14:00:00.000000000'))
