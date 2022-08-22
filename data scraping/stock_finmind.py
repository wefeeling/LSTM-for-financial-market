import requests
import pandas as pd
from typing import Dict, List


class StockFinMind():
    def __init__(self):
        self.base_url = 'https://api.finmindtrade.com/api/v4/data'

    def request_get(self, parameter):
        """送出 GET 請求

        :param parameter: 傳遞參數資料
        :return data: requests 回應資料
        """
        r = requests.get(self.base_url, params=parameter)
        if r.status_code != requests.codes.ok:
            print(f'網頁載入發生問題：{parameter}')
        try:
            data = r.json()
            if data['status'] != 200:
                print(f'回傳資料發生錯誤：{data["status"]}: {data["msg"]}')
                return None
        except Exception as e:
            print(e)
            return None
        return data["data"]

    def get_stock_deal_info(self, stock_id, start_date, end_date=None) -> List[Dict]:
        """股價日成交資訊 https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html

        :param stock_id: 股票代碼
        :param start_date: 開始日期
        :param end_date: 截止日期，不加則抓到前一個交易日
        :return data: 回應資料
        """
        parameter = {
            "dataset": "TaiwanStockPrice",
            "data_id": stock_id,
            "start_date": start_date,
            "end_date": end_date,
        }
        data = self.request_get(parameter)
        return data

    # def get_stock_history_info(self, stock_id, start_date=None) -> List[Dict]:
    #     """股票當日逐筆成交資訊

    #     :param stock_id: 股票代碼
    #     :param start_date: 指定日期
    #     :return data: 回應資料
    #     """
    #     parameter = {
    #         "dataset": "TaiwanStockPriceTick",
    #         "data_id": stock_id,
    #         "start_date": start_date,
    #     }
    #     data = self.request_get(parameter)
    #     return data

    # def get_stock_income_statement(self, stock_id, start_date, end_date=None) -> List[Dict]:
    #     """股票綜合損益表

    #     :param stock_id: 股票代碼
    #     :param start_date: 開始日期
    #     :param end_date: 截止日期，不加則抓到現在日期
    #     :return data: 回應資料
    #     """
    #     parameter = {
    #         "dataset": "TaiwanStockFinancialStatements",
    #         "data_id": stock_id,
    #         "start_date": start_date,
    #         "end_date": end_date
    #     }
    #     data = self.request_get(parameter)
    #     return data

    # def get_stock_dividend(self, stock_id, start_date) -> List[Dict]:
    #     """股利政策表

    #     :param stock_id: 股票代碼
    #     :param start_date: 指定日期
    #     :return data: 回應資料
    #     """
    #     parameter = {
    #         "dataset": "TaiwanStockDividend",
    #         "data_id": stock_id,
    #         "start_date": start_date
    #     }
    #     data = self.request_get(parameter)
    #     return data

    # def get_exchange_rate(self, currency, start_date) -> List[Dict]:
    #     """外幣對台幣匯率
    #     資料來源-台灣銀行(https://rate.bot.com.tw/xrt)

    #     :param currency: 外幣
    #     :param start_date: 指定日期
    #     :return data: 回應資料
    #     """
    #     parameter = {
    #         "dataset": "TaiwanExchangeRate",
    #         "data_id": currency,
    #         "start_date": start_date
    #     }
    #     data = self.request_get(parameter)
    #     return data


stock_finmind = StockFinMind()


# 股價日成交資訊
stock_deal_info = stock_finmind.get_stock_deal_info("2330", "2022-01-01", "2022-07-31")
# stock_deal_info = stock_finmind.get_stock_deal_info("2330", "2021-09-27")
# print(stock_deal_info)
data = pd.DataFrame(stock_deal_info)
print(data)

file_name = 'exchange_rate.csv' # 要記得後面加.xlsx
data.to_csv(file_name)

# # 股票當日逐筆成交資訊
# stock_history_info = stock_finmind.get_stock_history_info("2330", "2022-07-29")
# # print(len(stock_history_info))
# data = pd.DataFrame(stock_history_info)
# print(data.tail())  # 顯示最後五筆資料


# # 股票股票綜合損益表
# stock_income_statement = stock_finmind.get_stock_income_statement("2330", "2022-01-01", "2022-07-31")
# # print(len(stock_income_statement))
# data = pd.DataFrame(stock_income_statement)
# print(data)


# # 股利政策表
# stock_dividend = stock_finmind.get_stock_dividend("2330", "2022-01-01")
# # print(stock_dividend)
# print(len(stock_dividend))
# data = pd.DataFrame(stock_dividend)
# print(data.head())  # 顯示前五筆資料


# # 外幣對台幣匯率
# exchange_rate = stock_finmind.get_exchange_rate("USD", "2022-01-01")
# print(len(exchange_rate))
# data = pd.DataFrame(exchange_rate)
# print(data.tail())  # 顯示最後五筆資料


# 建立excel檔並輸出擷取的資料
# file_name = 'exchange_rate.xlsx' # 要記得後面加.xlsx
# data.to_excel(file_name)