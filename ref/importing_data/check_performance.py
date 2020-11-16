import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# read the performance summary dataframe
buy_and_hold_results = pd.read_pickle('buy_and_hold.pkl')


fig, ax = plt.subplots(3, 1, sharex=True, figsize=[16, 9])
# portfolio value
buy_and_hold_results.portfolio_value.plot(ax=ax[0])
ax[0].set_ylabel('portfolio value in €')

# asset
buy_and_hold_results.price.plot(ax=ax[1])
ax[1].set_ylabel('price in €')

# mark transactions
perf_trans = buy_and_hold_results.loc[[t != [] for t in buy_and_hold_results.transactions]]
buys = perf_trans.loc[[t[0]['amount'] > 0 for t in perf_trans.transactions]]
sells = perf_trans.loc[[t[0]['amount'] < 0 for t in perf_trans.transactions]]
ax[1].plot(buys.index, buy_and_hold_results.price.loc[buys.index], '^', markersize=10, color='g', label='buy')
ax[1].plot(sells.index, buy_and_hold_results.price.loc[sells.index], 'v', markersize=10, color='r', label='sell')

# daily returns
buy_and_hold_results.returns.plot(ax=ax[2])
ax[2].set_ylabel('daily returns')

fig.suptitle('Buy and Hold Strategy - ABN AMRO', fontsize=16)
plt.legend()
plt.savefig('sample_fig.png')

print('Final portfolio value (including cash): {}€'.format(np.round(buy_and_hold_results.portfolio_value[-1], 2)))


some_data = pd.DataFrame.from_records([x[0] for x in buy_and_hold_results.transactions.values if x != []])

print(buy_and_hold_results.columns)
print(some_data)