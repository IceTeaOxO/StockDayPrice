import requests
import pandas as pd
from dotenv import load_dotenv
import os
import DB

# 加載.env文件中的環境變數
load_dotenv()

# 使用os.getenv()方法獲取環境變數
key = os.getenv("FINMIND-KEY")
def call_taiwan_stockID():

    url = "https://api.finmindtrade.com/api/v4/data?"
    parameter = {
        "dataset": "TaiwanStockInfo",
        "token": key, # 參考登入，獲取金鑰
    }

    resp = requests.get(url, params=parameter)
    data = resp.json()
    return data

data = call_taiwan_stockID()
# 開啟DB
db = DB.StockDB("Stock.db")
# 因為會回傳多天資料，所以要用for一一拆開
data = data['data']
for day in data:
    #將字典變成list，只需要取值就好
    print(day)
    stockDay = list(day.values())
    db.insert_taiwan_stock_info_data("TaiwanStockID",stockDay)