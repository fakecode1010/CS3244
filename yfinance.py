import yfinance as yf
import pandas as pd
import numpy as np
#install using pip install yfinance
import os
os.chdir("D:\CS3244 project")
datasets=["NASDAQ2.txt","AMEX.txt"]
file=open(datasets[0],"r")
tickers=[]
while True:
    line=file.readline()
    if not line:
        break
    temp=(line.split(','))
    tickers.append(temp[0]);
print(tickers)
file.close()
os.chdir(r"D:\CS3244 project\data\NASDAQ")
#begin processing tickers
for i in range(0,len(tickers)):
    active_ticker=tickers[i]
    ticker_name=active_ticker
    ticker_name=ticker_name+".csv"
    active_ticker=yf.Ticker(active_ticker)
    hist=active_ticker.history(period="max",interval="1d",fmt="%s")
    hist.to_csv(ticker_name,header=True,index=True)
    #np.savetxt(ticker_name,hist,delimiter=",")
    hist=hist.iloc[0:0]

    









