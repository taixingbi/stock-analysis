import pandas as pd
import numpy as np
import yfinance
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

def test():
    print("test")

# interval = [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
def getTickerHistory(name, interval='1d', start= None, end= None, ): # data from finance 
    ticker = yfinance.Ticker(name)
    df = ticker.history(interval= interval, start= start, end= end)
    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].apply(mpl_dates.date2num)
    del df['Dividends']
    del df['Stock Splits']

    fixedCash = df['Close'][0]/len(df)
    df = addFixedInvestment(df, fixedCash)
    return df

def addFixedInvestment(df, fixedCash):
    df['RecurringInvestment'] = fixedCash 
    df_daily_returns = (df['Close'].pct_change()+1).to_list()
    df_daily_returns[0] = 1
    
    for i, df_daily_return in enumerate(df_daily_returns):
        if i==0 : continue
        df['RecurringInvestment'][i] += df['RecurringInvestment'][i-1] * df_daily_return

    return df


if __name__ == "__main__":
    name = "NRDS"  # rate= 0.94

    start = "2020-01-01"
    end = "2021-10-28" 
    interval = '1h'
    df = getTickerHistory(name, start, end, interval)
    # # df = df[:5]
    # print(df)

    # df = addFixedInvestment(df, 100)
    print(df)

