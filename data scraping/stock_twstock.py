import twstock
import pandas as pd
import requests
import time
# import yfinance as yf
# 導入twstock及pandas模組，pandas模組縮寫為pd
# 取得證交所股票data

# 查看交易所商品清單
tickers = twstock.twse
df_tickers = pd.DataFrame(tickers).T

# 判斷股票是否在清單裡面
'2890' in tickers

# 取得證交所股票data
stock_2890 = twstock.Stock('2890')
symbol = stock_2890.sid # 回傳股票代號
close = stock_2890.price # 收
startTime = '2022-01-01'
endTime = '2022-08-03'
 
print(stock_2890)
# filename = 'C:\\Users\\user\\Desktop\\TEST\\2890_0803.csv'
# df_realtime.to_csv(filename)