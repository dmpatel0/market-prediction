import json
import time
import pandas as pd
import yfinance as yf
from tqdm import tqdm
import logging

logger = logging.getLogger('yfinance')
logger.disabled = True
logger.propagate = False

# A list of initial companies to include
tickers = ['NVDA', 'AAPL', 'TSLA', 'MSFT', 'GOOG', 'AMZN', 'META', 'DIS', 'PYPL']
df_list = []


with open('cik_to_tickers.json', "r") as file:
    data = json.load(file)
    for ticker in data.values():
        if ticker[0] not in tickers:
            tickers.append(ticker[0])

def request_data(i_start, i_end):
    for i in tqdm(range(i_start, i_end), desc="Fetching Data"):
        ticker = tickers[i]
        stock = yf.Ticker(ticker)
        stock_df = stock.history(period='10y', interval='1wk')
        stock_df['Ticker'] = ticker
        df_list.append(stock_df)
    
    for _ in tqdm(range(90), desc="Sleeping..."):
        time.sleep(1)

request_data(0, 500)
request_data(500, 1000)
request_data(1000, 1500)
request_data(1500, 2000)

master_df = pd.concat(df_list)
master_df.head()
master_df.shape

master_df.to_csv('master_stock_dataset.csv')