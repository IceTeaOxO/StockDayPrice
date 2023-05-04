#    data = call_day_price("2330","2020-04-06","2020-04-08")
# 2311日月光,2330台積電,2454聯發科,3034聯詠,6770力積電
import time
# from finmindStockDayPrice import call_day_price
from finmindStockTick import call_tick
from datetime import datetime, timedelta
# 設置要執行的次數
total_runs = 5
# 設置每次執行之間的時間間隔
time_interval = 10 # 時間間隔，單位為秒
# 設置計數器
count = 0

# 設定要爬的stock_id
ID = ["2311","2330","2454","3034","6770"] 

# 設定開始、終結日期
startDate = datetime.strptime("2022-01-01", "%Y-%m-%d")
endDate = datetime.strptime("2022-01-05", "%Y-%m-%d")

# 進入無限循環，直到執行次數達到設置值
while count < total_runs:
    while startDate <= endDate:
        print("執行操作")
        print(ID[count])
        # 將日期格式改為"%Y-%m-%d"
        startDate_str = startDate.strftime("%Y-%m-%d")
        # print(startDate_str)
        #尚未超過API數，暫不處理一次請求超過數量
        call_tick(ID[count],startDate_str)
        # print(startDate.strftime("%Y-%m-%d"))
        startDate += timedelta(days=1)
    # 執行您要自動執行的操作
    

    # 增加計數器
    count += 1

    # 等待設置的時間間隔
    time.sleep(time_interval)

print("自動執行完成")
