### To run

Equivalent logic would be 

```
%%zipline --start 2017-1-2 --end 2017-12-29 --capital-base 250 --bundle eu_stocks -o buy_and_hold.pkl --trading-calendar XAMS
```

Ends up as 

```
zipline run --start 2017-1-2 --end 2017-12-29 --capital-base 250 --bundle eu_stocks -o buy_and_hold.pkl --trading-calendar XAMS --benchmark-symbol AEX -f buy_and_hold.py
```


This is a simple example to get a bundle into zipline for analyze.

### Steps to run importing_data

1. run import_data.py - this extracts csvs to data
2. move extension.py to `~/.zipline/extension.py
3. run script to analyze data
  * run buy_and_hold.py
    - run check_performance.py
  * run sma_strategy.py
    - generates plots