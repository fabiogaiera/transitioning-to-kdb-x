import os

import pykx as kx

from tick_architecture.hdb.strategy import Strategy
from utils.timing import log_execution_time


# Usage for trades: create_or_update_table(csv_file_path, database_path, table_name, StrategyTrades())
# Usage for quotes: create_or_update_table(csv_file_path, database_path, table_name, StrategyQuotes())
def create_or_update_table(csv_file_path, database_path, table_name, strategy: Strategy):
    # Upload CSV file into the table
    table = strategy.execute(csv_file_path)

    # Add the column date doing a casting
    table['date'] = table['timestamp'].date

    # Initialize an instance of DB class
    db = kx.DB(path=database_path, overwrite=True)

    #  Create an on-disk partitioned table within a kdb+ database from a supplied pykx.wrappers.Table
    db.create(table=table, table_name=table_name, partition='date')


@log_execution_time
def create_database(csv_file_folder, database_path, table_name, strategy: Strategy):
    with os.scandir(csv_file_folder) as csv_files:
        # Iterate through CSV directory
        for csv_file in csv_files:
            # Invoke create_or_update_table function
            create_or_update_table(csv_file.path, database_path, table_name, strategy)
