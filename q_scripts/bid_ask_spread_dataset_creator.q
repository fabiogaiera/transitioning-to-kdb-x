/ CSV format example for trades
/ timestamp,sym,price,size
/ 2025.05.05D08:00:00.009039359,IBM,244.56,10
/ 2025.05.05D08:00:00.156501572,IBM,243,8
/ 2025.05.05D08:00:00.156579644,IBM,244.03,6

/ CSV format example for quotes
/ timestamp,sym,bid_price,bid_size,ask_price,ask_size
/ 2025.05.23D08:00:00.001037561,IBM,257.03,2,260.91,1
/ 2025.05.23D08:00:00.001062570,IBM,257.03,2,259.77,1
/ 2025.05.23D08:00:00.009487606,IBM,257.03,2,259.49,1
/ 2025.05.23D08:00:00.017576775,IBM,257.03,2,259.41,1

/ createTable: Load trades from CSV and compute OHLCV during market hours
/ Parameters:
/   csvTradesPath         - Path to the CSV file with trades data
/   csvQuotesPath         - Path to the CSV file with quotes data
/   marketOpenDateTime    - e.g. 2025.06.16D13:30:00.000000000
/   marketCloseDateTime   - e.g. 2025.06.16D20:00:00.000000000
/ Returns:
/   Maximum Effective Bid-Ask Spread
createTable:{[csvTradesPath;csvQuotesPath;marketOpenDateTime;marketCloseDateTime]

    / Use 0: with explicit types and comma delimiter; path cast to symbol

    / Load CSV file: columns expected in order - timestamp (P), symbol (S), float (F), long (J)
    trades:("PSFJ";enlist ",") 0: csvTradesPath;

    / Load CSV file: columns expected in order - timestamp (P), symbol (S), float (F), long (J), float (F), long (J)
    quotes:("PSFJFJ";enlist ",") 0: csvQuotesPath;

    / Filter trades and quotes to those occurring strictly within market hours (inclusive)
    trades:select from trades where timestamp within (marketOpenDateTime;marketCloseDateTime);
    quotes:select from quotes where timestamp within (marketOpenDateTime;marketCloseDateTime);

    / Applying attributes
    quotes:update `g#sym from quotes;

    / As-Of Join between trades and quotes
    taq:aj[`sym`timestamp; trades; quotes];

    / Filter only rows that do not contain nulls
    taq:select from taq where not any null each flip taq;

    / Calculate mid price
    mp:update mid_price:(bid_price+ask_price)%2 from taq;

    / Calculate the maximum effective bid-ask spread (Percentage Form) every 15 minutes
    bas:select bid_ask_spread:max 2*(abs (price-mid_price)%mid_price)*100 by time:15 xbar timestamp.minute from mp;

    / Return the table
    bas

 }

default_args:`param1`param2`param3`param4!(`$"/path/to/trades/IBM.csv";`$"/path/to/quotes";2025.06.16D13:30;2025.06.16D20)

args:.Q.def[default_args] .Q.opt[.z.x]

show args

/ bas:createTable[args[`param1]; args[`param2]; args[`param3]; args[`param4]]
bas:createTable . args`param1`param2`param3`param4

/ Open TCP port 5002 for q connections
\p 5002