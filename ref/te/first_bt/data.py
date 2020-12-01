# importing_data
# Inspired by https://github.com/erykml/medium_articles/blob/master/Quantitative%20Finance/introduction_to_backtesting_eur_stocks.ipynb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from yahoofinancials import YahooFinancials
import warnings
import pathlib
import os

plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = [16, 9]
plt.rcParams['figure.dpi'] = 200
warnings.simplefilter(action='ignore', category=FutureWarning)

def download_csv_data(ticker, start_date, end_date, freq, path):
    
    yahoo_financials = YahooFinancials(ticker)

    df = yahoo_financials.get_historical_price_data(start_date, end_date, freq)
    df = pd.DataFrame(df[ticker]['prices']).drop(['date'], axis=1) \
            .rename(columns={'formatted_date':'date'}) \
            .loc[:, ['date','open','high','low','close','volume']] \
            .set_index('date')
    df.index = pd.to_datetime(df.index)
    df['dividend'] = 0
    df['split'] = 1

    # save data to csv for later ingestion
    df.to_csv(path, header=True, index=True)

    # plot the time series
    df.close.plot(title='{} prices --- {}:{}'.format(ticker, start_date, end_date))

workspace = '/root/workspace/zipline-experiments'
folder_path = f'{workspace}/data/tsx/daily'
pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
# need to validate start_dates with actual ticker dates
download_csv_data(ticker='DCM.TO', 
                  start_date='2019-09-01', 
                  end_date='2020-11-29', 
                  freq='daily', 
                  path=f'{folder_path}/dcm.csv')
