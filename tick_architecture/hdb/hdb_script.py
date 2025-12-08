import sys

from tick_architecture.hdb.hdb_creator import create_database
from tick_architecture.hdb.strategy import StrategyQuotes
from tick_architecture.hdb.strategy import StrategyTrades

csv_trades_path = sys.argv[1]
trades_table_name = sys.argv[2]
csv_quotes_path = sys.argv[3]
quotes_table_name = sys.argv[4]
database_path = sys.argv[5]

if __name__ == '__main__':
    create_database(csv_trades_path, database_path, trades_table_name, StrategyTrades())
    create_database(csv_quotes_path, database_path, quotes_table_name, StrategyQuotes())
