import sys

from trades_historical_database.returns_table_creator import create_table_returns
from trades_historical_database.trades_historical_database_creator import create_database
from trades_historical_database.trades_historical_database_creator import run_query

if __name__ == '__main__':

    if len(sys.argv) != 8:
        print("Incorrect parameters")
        sys.exit(1)

    csv_path = sys.argv[1]
    database_path = sys.argv[2]
    table_name = sys.argv[3]
    start_date = sys.argv[4]
    end_date = sys.argv[5]
    market_open_timespan = sys.argv[6]
    market_close_timespan = sys.argv[7]

    create_database(csv_path, database_path, table_name)

    dataframe = run_query(database_path,
                          table_name,
                          start_date,
                          end_date,
                          market_open_timespan,
                          market_close_timespan)

    create_table_returns(dataframe)
