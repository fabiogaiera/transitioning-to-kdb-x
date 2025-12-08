import sys

import pykx as kx

from tick_architecture.rdb_schema import quotes
from tick_architecture.rdb_schema import trades

db_dir = sys.argv[1]
logs_dir = sys.argv[2]

db = kx.DB(path=db_dir)

print(db.tables)

basic = kx.tick.BASIC(
    tables={'trades': trades, 'quotes': quotes},
    ports={'tickerplant': 5010, 'rdb': 5012, 'hdb': 5011},
    log_directory=logs_dir,
    database=db_dir)

chained_tp = kx.tick.TICK(port=5013, chained=True)

# Requisites For Fedora Linux:

# $ sudo dnf install python3-devel
# source .venv/bin/activate
# python -c "import pykx;pykx.install_into_QHOME()"

# To verify it works:

# Open a q session
# \l pykx.q

if __name__ == '__main__':
    basic.start()
    chained_tp.start({'tickerplant': 'localhost:5010'})
