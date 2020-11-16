### To run

Equivalent logic would be 

```
%%zipline --start 2017-1-2 --end 2017-12-29 --capital-base 250 --bundle eu_stocks -o buy_and_hold.pkl --trading-calendar XAMS
```

Ends up as 

```
zipline run --start 2017-1-2 --end 2017-12-29 --capital-base 250 --bundle eu_stocks -o buy_and_hold.pkl --trading-calendar XAMS --benchmark-symbol AEX -f buy_and_hold.py
```
