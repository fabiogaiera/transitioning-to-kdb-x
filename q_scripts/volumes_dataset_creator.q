/ CSV format example for trades
/ timestamp,sym,price,size
/ 2025.05.05D08:00:00.009039359,IBM,244.56,10
/ 2025.05.05D08:00:00.156501572,IBM,243,8
/ 2025.05.05D08:00:00.156579644,IBM,244.03,6

/ createTable: Load trades from CSV and compute hourly trade volume during market hours
/ Parameters:
/   csvTradesPath         - Path to the CSV file containing trade data (as symbol)
/   marketOpenTime        - e.g. 2025.06.06D13:30:00.000000000
/   marketCloseTime       - e.g. 2025.06.06D20:00:00.000000000
/ Returns:
/   Table with hourly buckets and trade count per hour
createTable:{[csvTradesPath;marketOpenTime;marketCloseTime]

    / Use 0: with explicit types and comma delimiter; path cast to symbol

    / Load CSV file: columns expected in order - timestamp (P), symbol (S), float (F), long (J)
    trades:("PSFJ";enlist ",") 0: csvTradesPath;

    / Filter trades to include only those executed within market hours (inclusive)
    trades:select from trades where timestamp within (marketOpenTime;marketCloseTime);

    / Aggregate trade count by hour: bucket minute-level timestamps into 1-hour intervals
    / xbar with 60 aligns minutes to the start of each hour (e.g., 09:15 falls into 09:00)
    tv:select tc:count i by time:60 xbar timestamp.minute from trades;

    / Return hourly trade volume table
    tv

 }

default_args:`param1`param2`param3!(`$"/path/to/trades/IBM.csv";2025.06.06D13:30;2025.06.06D20)

args:.Q.def[default_args] .Q.opt[.z.x]

show args

/ tv:createTable[args[`param1]; args[`param2]; args[`param3]]
tv:createTable . args`param1`param2`param3

/ Open TCP port 5000 for q connections
\p 5000