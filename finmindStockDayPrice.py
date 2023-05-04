import requests
import pandas as pd
from dotenv import load_dotenv
import os
import DB
from test import getTWStockID
import time
# 加載.env文件中的環境變數
load_dotenv()

# 使用os.getenv()方法獲取環境變數
key = os.getenv("FINMIND-KEY")
def call_day_price(data_id,start_date,end_date):

    url = "https://api.finmindtrade.com/api/v4/data?"
    parameter = {
        "dataset": "TaiwanStockPrice",
        "data_id": data_id,
        "start_date": start_date,
        "end_date": end_date,
        "token": key, # 參考登入，獲取金鑰
    }
    resp = requests.get(url, params=parameter)
    data = resp.json()

    # data = call_day_price(data_id,start_date,end_date)

    # 開啟DB
    db = DB.StockDB("Stock.db")
    # 因為會回傳多天資料，所以要用for一一拆開
    # print(data)
    data = data['data']
    for day in data:
        #將字典變成list，只需要取值就好
        # print(day)
        stockDay = list(day.values())
        db.insert_day_price_data("StockDayPrice",stockDay)
    print("completed!")


# 設定要爬的stock_id
# ID = ["2311","2330","2454","3034","6770"] 

for i in range(0,len(getTWStockID(9999,0)),580):
    ID = getTWStockID(limit=580,offset=i)

    # 設定開始、終結日期
    startDate = "2010-01-01"
    endDate = "2021-12-31"
    for stock_id in ID:
        # print(type(stock_id))
        call_day_price(stock_id[0],startDate,endDate)
    time.sleep(3601)

# data = pd.DataFrame(data["data"])
# print(data.head())