import pandas_datareader as pdr
import time 


df_2610 = pdr.DataReader('2610.TW', 'yahoo')
# df_2885 = pdr.DataReader('2885.TW', 'yahoo')

startTime = '2022-01-01'
endTime = '2022-08-06'


df_2610 = pdr.DataReader('2610.TW', 'yahoo', startTime, endTime)
# df_2885 = pdr.DataReader('2885.TW', 'yahoo', startTime,endTime )

filename2 = "df_2610.csv"
# filename3 = 'df_2885.csv'

df_2610.to_csv(filename2)
# df_2610.to_csv(filename3)