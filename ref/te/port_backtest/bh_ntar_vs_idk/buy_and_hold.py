from zipline.api import order, symbol, record, set_benchmark
from zipline import run_algorithm
import pandas as pd
import matplotlib.pyplot as plt
# parameters
selected_stock = 'NTAR'
n_stocks_to_buy = 10

def initialize(context):
    set_benchmark(symbol('IDK'))
    context.asset = symbol('NTAR')
    context.has_ordered = False  

def handle_data(context, data):
    # record price for further inspection
    record(price=data.current(symbol(selected_stock), 'price'))
    
    # trading logic
    if not context.has_ordered:
        # placing order, negative number for sale/short
        order(symbol(selected_stock), n_stocks_to_buy)
        # setting up a flag for holding a position
        context.has_ordered = True


def analyze(context, perf):
    fig = plt.figure(figsize=(12, 8))
    
    # First chart
    ax = fig.add_subplot(311)
    ax.set_title('Strategy Results')
    ax.semilogy(perf['portfolio_value'], linestyle='-', 
                label='Equity Curve', linewidth=3.0)
    ax.legend()
    ax.grid(False)
    
    # Second chart
    ax = fig.add_subplot(312)
    ax.plot(perf['gross_leverage'], 
            label='Exposure', linestyle='-', linewidth=1.0)
    ax.legend()
    ax.grid(True)

    # Third chart
    ax = fig.add_subplot(313)
    ax.plot(perf['returns'], label='Returns', linestyle='-.', linewidth=1.0)
    ax.legend()
    ax.grid(True)
    fig.savefig('zp_dcm.png')

# Set start and end date
# start_date = datetime(2019, 9, 3, tzinfo=pytz.UTC)
# end_date = datetime(2020, 11, 27, tzinfo=pytz.UTC)
# pandas compilant timestamp
# need to start early because of 100 day rolling window
start_date = pd.Timestamp('2019-06-01', tz='utc')
end_date = pd.Timestamp('2020-11-27', tz='utc')
# Fire off the backtest
results = run_algorithm(
    start=start_date, 
    end=end_date, 
    initialize=initialize, 
    analyze=analyze, 
    handle_data=handle_data, 
    capital_base=10000, 
    bundle='bt_ntaridk' 
)