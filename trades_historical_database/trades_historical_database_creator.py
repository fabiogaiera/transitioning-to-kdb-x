import os

import pykx as kx

from utils.timing import log_execution_time


def create_or_update_table(csv_file_path, database_path, table_name):
    # Upload CSV file into trades table
    trades_table = kx.q.read.csv(csv_file_path, [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])

    # Add the column date doing a casting
    trades_table['date'] = trades_table['timestamp'].date

    # Initialize an instance of DB class
    db = kx.DB(path=database_path, overwrite=True)

    #  Create an on-disk partitioned table within a kdb+ database from a supplied pykx.wrappers.Table
    db.create(table=trades_table, table_name=table_name, partition='date')


@log_execution_time
def create_database(csv_file_folder, database_path, table_name):
    with os.scandir(csv_file_folder) as csv_files:
        # Iterate through CSV directory
        for csv_file in csv_files:
            # Invoke create_or_update_table function
            create_or_update_table(csv_file.path, database_path, table_name)


@log_execution_time
def run_query(database_path, table_name, start_date, end_date, market_open, market_close):
    # Initialize an instance of DB class
    db = kx.DB(path=database_path, overwrite=True)

    # Once the database is created, we can retrieve the table using the getattr function
    table = getattr(db, table_name)

    # Filter by market hours
    close_price = table.select(

        columns={'close': kx.Column('price').last()},

        where=((kx.Column('date').within(kx.q(start_date), kx.q(end_date))) &
               (kx.Column('timestamp').within(kx.q(market_open), kx.q(market_close)))
               ),

        by=kx.Column('date')

    )

    # Calculate return price
    return_price = close_price.update(
        kx.Column('return', value=(kx.Column('close').divide(kx.Column('close').prev()) - 1))
    )

    # Return an instance of pandas DataFrame
    return return_price.pd()
