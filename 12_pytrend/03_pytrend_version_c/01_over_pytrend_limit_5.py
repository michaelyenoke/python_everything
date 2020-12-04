# 第一步：Python爬取資料 - 超過 google 查詢上限的方法

from pytrends.request import TrendReq
from pprint import pprint
from time import sleep
import pandas as pd
import datetime
import numpy as np
import json
import csv


#  ,'獨輪車',登山車','火車','梨泰院','新冠','新垣結衣','男性自行車'
data = ['陳時中','環島']
#有些詞彙沒有搜尋熱度 - 暫不處理 '男性自行車','武漢肺炎','女性自行車'
#print(len(data)-1)
pList = []


for keywords in data:
    #print(keywords)
    keywords_list = [keywords]
    pytrend = TrendReq(hl='en-US', tz=360)
    pytrend.build_payload(keywords_list, cat=0, timeframe='today 5-y', geo='TW', gprop='')
    interest_over_time_df = pytrend.interest_over_time()[keywords]
    pList.append(interest_over_time_df)



    
#print(type(pList))
pList_df = pd.DataFrame(pList)

# 欄與列的整理
df3 = pList_df.stack(0)
df4 = df3.unstack(0)
#print(len(df4))

#df4.head()

#print(df4)


# df4["陳時中"] = df4["陳時中"].replace(0,99) # 不是字串,不用.str

#print(len(df4.iloc[ : ]))

# 匯成JSON檔案
#preload = json.loads(df4.to_json(orient='table'))
#print(json.dumps(preload, ensure_ascii=False))


## 輸出
#print(len(pList))
#print(pList_df)
#df4.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile2')
