import os

from trades_historical_database.returns_table_creator import create_table_returns
from trades_historical_database.trades_historical_database_creator import run_query

user = os.getlogin()
db_path = f"/home/{user}/DB"
t_name = "trades"
s_date = "2025.04.01"
e_date = "2025.04.30"
mkt_open_timespan = "13:30:00.000000000"
mkt_close_timespan = "20:00:00.000000000"

dataframe = run_query(db_path,
                      t_name,
                      s_date,
                      e_date,
                      mkt_open_timespan,
                      mkt_close_timespan)

create_table_returns(dataframe)
