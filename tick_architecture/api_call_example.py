from tick_architecture.real_time_processor_starter import rtp

if __name__ == '__main__':
    print("There should be results")
    print(rtp('count_ticks', 'trades', 'AAPL', '13:30:00.000000000', '20:00:00.000000000'))
    print(rtp('count_ticks', 'quotes', 'AAPL', '13:30:00.000000000', '20:00:00.000000000'))
    print("There should not be results")
    print(rtp('count_ticks', 'trades', 'AAPL', '23:30:00.000000000', '23:55:00.000000000'))
    print(rtp('count_ticks', 'quotes', 'AAPL', '23:30:00.000000000', '23:55:00.000000000'))
