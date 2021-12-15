import pandas as pd
import numpy as np
import yfinance
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates

def isSupport(df, i):
  support = df['Low'][i] < df['Low'][i-1]  and df['Low'][i] < df['Low'][i+1] and df['Low'][i+1] < df['Low'][i+2] and df['Low'][i-1] < df['Low'][i-2]
  return support

def isResistance(df, i):
  resistance = df['High'][i] > df['High'][i-1]  and df['High'][i] > df['High'][i+1] and df['High'][i+1] > df['High'][i+2] and df['High'][i-1] > df['High'][i-2]
  return resistance


name = 'TQQQ'
ticker = yfinance.Ticker(name)
df = ticker.history(interval="1d", start="2021-08-03", end="2021-10-29")

df['Date'] = pd.to_datetime(df.index)
df['Date'] = df['Date'].apply(mpl_dates.date2num)
df = df.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
df.head()

def toDate(i):
    return str(df.index[i]).split(" ")[0]

levels_support = []
for i in range(2, df.shape[0]-2):
  if isSupport(df,i):
    levels_support.append((i,df['Low'][i], toDate(i), "support"))

levels_resistance = []
for i in range(2, df.shape[0]-2):  
  if isResistance(df,i):
    levels_resistance.append((i,df['High'][i], toDate(i), "resistance"))

print("\n-------support---------")
for level in levels_support:
    print(level)

print("\n-------resistance---------")
for level in levels_resistance:
    print(level)



print("done")