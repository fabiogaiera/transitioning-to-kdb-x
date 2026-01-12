from tick_architecture.real_time_processor_starter import rtp

if __name__ == '__main__':
    print(rtp('count_ticks', 'trades', 'AAPL', '00:30:00.000000000', '23:00:00.000000000'))
    print(rtp('count_ticks', 'quotes', 'AAPL', '00:30:00.000000000', '23:00:00.000000000'))