import matplotlib.pyplot as plt # Graphing
import pandas as pd # Pandas
import numpy as np # NumPy
import requests
import yfinance as yf
from datetime import datetime, timedelta

# Get Stock Data
def getStockData(Ticker, TimePeriod):
  stock = yf.Ticker(Ticker) #Getting a Stock
  data = stock.history(period=TimePeriod) #Getting Stock History From A Certain Point
  data.reset_index(inplace=True)
  data['Date'] = data['Date'].astype(str).str[:10]
  return data


def getDailyReturns(Ticker, TimePeriod):
  data = getStockData(Ticker, TimePeriod)
  data['Daily_Return'] = data['Close'].pct_change() * 100
  return data.dropna()

