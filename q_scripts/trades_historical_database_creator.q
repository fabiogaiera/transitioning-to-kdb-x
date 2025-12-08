/ CSV format example
/ timestamp,sym,price,size
/ 2025.05.05D08:00:00.009039359,IBM,244.56,10
/ 2025.05.05D08:00:00.156501572,IBM,243,8
/ 2025.05.05D08:00:00.156579644,IBM,244.03,6

/ insertRecords: Load trades from CSV files create a historical database of trades
/ Parameters:
/   csvTradesPath         - Path to the CSV file with trades data
/   dbTradesPath          - Path to the historical database of trades
insertRecords:{[csvTradesPath;dbTradesPath]

    / Use 0: with explicit types and comma delimiter; path cast to symbol

    / Load CSV file: columns expected in order - timestamp (P), symbol (S), float (F), long (J)
    tradesData:("PSFJ";enlist ",") 0: csvTradesPath;

    / Extract the date for partitioning (CSV files contain ticks for a single date)
    partitionDate:`date$tradesData[0; `timestamp];

    / Assign trades to a global variable
    `trades set tradesData;

    / Save the table to a partitioned database
    .Q.dpft[dbTradesPath; partitionDate; `sym; `trades];

 }

/ Take the first command-line argument, interpret it as a string, convert it to a symbol, then open it as a handle
pathToCSVFiles:hsym `$.z.x 0;
/ Take the second command-line argument, interpret it as a string, convert it to a symbol, then open it as a handle
pathToHDB:hsym `$.z.x 1;
/ Get full paths to all files in a directory
absPaths:{.Q.dd[x] each key x} pathToCSVFiles;
/ Invoke the function for each path from absPaths
\t insertRecords[; pathToHDB] each absPaths;
/ Exit. Nothing more to do.
exit 0