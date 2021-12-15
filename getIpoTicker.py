import pandas as pd
import numpy as np
import yfinance
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

filename = "ipo.txt"

tickers =[]
dates = []
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        ticker = line.split()[3]
        date = line.split()[0] + " " + line.split()[1][:-1] + " " + line.split()[2]
        dates.append(date)
        tickers.append(ticker)

d = {'Date': dates, 'IPO': tickers}
df = pd.DataFrame(data=d)
df.to_csv("ipo.csv", sep=',')

print(df)




def get_ipo_robin_5min_valid():
    tickers_filter= []
    dates_filter= []
    for i , ticker in enumerate(tickers):
        try:
            rs.stocks.get_stock_historicals(ticker, interval="5minute", span="day")
            tickers_filter.append(ticker)
            dates_filter.append( dates[i])
        except:
            print(ticker)
            continue

    d = {'Date': dates_filter, 'IPO': tickers_filter}
    df = pd.DataFrame(data=d)
    df.to_csv("ipo_robin_5min_valid.csv", sep=',')