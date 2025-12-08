/ CSV format example for trades
/ timestamp,sym,price,size
/ 2025.05.05D08:00:00.009039359,IBM,244.56,10
/ 2025.05.05D08:00:00.156501572,IBM,243,8
/ 2025.05.05D08:00:00.156579644,IBM,244.03,6

/ createTable: Load trades from CSV and compute OHLCV during market hours
/ Parameters:
/   csvTradesPath         - Path to the CSV file with trades data
/   marketOpenTime        - e.g. 13:30:00.000000000
/   marketCloseTime       - e.g. 20:00:00.000000000
/ Returns:
/   OHLCV table
createTable:{[csvTradesPath;marketOpenTime;marketCloseTime]

    / Use 0: with explicit types and comma delimiter; path cast to symbol

    / Load CSV file: columns expected in order - timestamp (P), symbol (S), float (F), long (J)
    trades:("PSFJ";enlist ",") 0: csvTradesPath;

    / Extract date part from timestamp for grouping
    trades:update date:`date$timestamp from trades;

    / Build full market-open and market-close timestamps for each trading day
    trades:update mo:date+marketOpenTime, mc:date+marketCloseTime from trades;

    / Filter trades to those occurring strictly within market hours (inclusive)
    trades:select from trades where timestamp within (mo;mc);

    / Aggregate OHLCV per date:
    /   open   - price of the first trade of the day
    /   high   - highest price during the day
    /   low    - lowest price during the day
    /   close  - price of the last trade of the day
    /   volume - total size (sum of all trade sizes)
    ohlcv:select
            open:first price,
            high:max price,
            low:min price,
            close:last price,
            volume:sum size
              by date from trades;

    / Return the aggregated OHLCV table
    ohlcv
 }

/ https://code.kx.com/q/ref/tok/
/ Invoke function with command-line arguments:
/   .z.x 0 CSV file path
/   .z.x 1 market open  time
/   .z.x 2 market close time
/ ohlcv:createTable["S"$.z.x 0; "N"$.z.x 1; "N"$.z.x 2]

default_args:`param1`param2`param3!(`$"/path/to/trades/IBM.csv";13:30:00.000000000;20:00:00.000000000)

args:.Q.def[default_args] .Q.opt[.z.x]

show args

/ ohlcv:createTable[args[`param1]; args[`param2]; args[`param3]]
ohlcv:createTable . args`param1`param2`param3

/ Listen for incoming q connections on TCP port 5001
\p 5001