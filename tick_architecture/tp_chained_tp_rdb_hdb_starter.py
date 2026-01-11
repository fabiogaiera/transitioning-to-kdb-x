import sys

import pykx as kx

from tick_architecture.api import count_ticks
from tick_architecture.rdb_schema import quotes
from tick_architecture.rdb_schema import trades

db_dir = sys.argv[1]
logs_dir = sys.argv[2]

db = kx.DB(path=db_dir)

print(db.tables)

basic = kx.tick.BASIC(
    tables={'trades': trades, 'quotes': quotes},
    ports={'tickerplant': 5010, 'rdb': 5011, 'hdb': 5012},
    log_directory=logs_dir,
    database=db_dir)

chained_tp = kx.tick.TICK(port=5013, chained=True)

# Requisites For Fedora Linux:
# $ sudo dnf install python3-devel

# Requisites For Ubuntu Linux:
# $ sudo apt install libpython3.11-dev

# source .venv/bin/activate
# python -c "import pykx;pykx.install_into_QHOME()"

# To verify it works:

# Open a q session
# \l pykx.q

# Official documentation: https://code.kx.com/kdb-x/get_started/kdb-x-python-install.html

if __name__ == '__main__':
    basic.start()
    basic.hdb.register_api('count_ticks', count_ticks)
    chained_tp.start({'tickerplant': 'localhost:5010'})
