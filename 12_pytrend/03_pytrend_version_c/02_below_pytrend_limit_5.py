# 第一步：Python爬取資料 - 不超過 google 查詢上限可行

from pytrends.request import TrendReq
from pprint import pprint
from time import sleep
import pandas as pd
import json
import csv


# 超過 5 個 Google 不給回應,需要寫迴圈
# 5年方面則是沒有問題


keywords_list = ['男性自行車','環島','迪卡儂','女性自行車','獨輪車','摩托車','登山車']
#print(len(keywords_list))
#print(keywords_list[2])
total_list = []
df_list = []



for i in range(0,len(keywords_list)-1): 
    #print(len(keywords_list)-1)
    y = keywords_list[i]
    x.append(y)
    #print(y)
    pytrend = TrendReq(hl='en-US', tz=360)
    pytrend.build_payload(kw_list=x, cat=0, timeframe='today 5-y', geo='TW', gprop='') #自帶取出字串功能,所以用[i]會變成個別的字
    interest_over_time_df = pytrend.interest_over_time()
    #print(interest_over_time_df)   
    #print 出來雖然keywords都有出現,但輸出成csv的時候就只有一個,需要 .append()
    #print(type(interest_over_time_df))
    total_list.append(interest_over_time_df)     #e改用extend p.6-28
    
    
#print(len(total_list))
#print(type(total_list))
print(total_list)
#print(total_list[2])
    

#for j in range(len(total_list)):
#    df_list.append(total_list[j])


#print(df_list)

    
    
# 輸出 csv 格式
#total_list_df = pd.DataFrame(total_list)
#print(type(total_list_df))
#total_list_df.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile')
    # 輸出 JSON
    #preload = json.loads(pytrend.interest_over_time().to_json(orient='table'))['data']
    #print(json.dumps(preload, ensure_ascii=False))    
    
    # 匯成JSON檔案
    #preload = json.loads(pytrend.interest_over_time().to_json(orient='table'))['data']
    #print(json.dumps(preload, ensure_ascii=False))
    
    # 匯成CSV檔至本機
    #interest_over_time_df.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile')
