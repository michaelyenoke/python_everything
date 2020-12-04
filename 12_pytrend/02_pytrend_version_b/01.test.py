# 第一步：Python爬取資料 - 超過 google 查詢上限的方法

from pytrends.request import TrendReq
from pprint import pprint
from time import sleep
from datetime import datetime # import datetime classs from datetime module
import pandas as pd
import numpy as np
import json
import csv


dt_3 = []

#  ,'獨輪車','登山車','火車','梨泰院','新冠','新垣結衣'
data = ['陳時中','環島','獨輪車','登山車','火車','梨泰院','新冠','新垣結衣']
#有些詞彙沒有搜尋熱度 - 暫不處理 '男性自行車','武漢肺炎','女性自行車','男性自行車'
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


# 將index.name的date改成column
df4.reset_index(inplace=True)
print(df4)
#print(type(df4))


# 將日期單獨抽離出來並從 timeframe - datetime - string

d = []

# 將日期單獨抽離出來,格式 timeframe
df4_date = df4['date']
#print(df4_date[0])
#print(type(df4_date[0]))

for i in range(0,len(df4)):
    # 將timeframe 轉換成 datetime
    date_time_obj = datetime.strptime(str(df4_date[i]), '%Y-%m-%d %H:%M:%S') 
    #print(date_time_obj)
    #print(type(date_time_obj))
    # 將 datetime 轉換成 string, 並拆開
    d.append(date_time_obj.strftime("%Y,%b").split())
    #print(type(d))

#print(d)
#print(d[0][0])
#print(type(d[0][0]))


box_1 = []
box_2 = []


for j in range(0,len(d)):
    d_sp = d[j][0].split(",",1)
    d_sp_y = d_sp[0]
    d_sp_m = d_sp[1]
    box_1.append(d_sp_y)
    box_2.append(d_sp_m)
    #print(type(d_sp))


#print(box_1)
#print(len(box_1)) 
#print(type(box_1))
box_1_df = pd.DataFrame(box_1)
#print(type(box_1_df))
#print(box_1_df)
box_1_df.rename(columns = {0: "year"},  inplace=True)
#print(box_1_df)

#print(box_2)
#print(len(box_2))
#print(type(box_2))
box_2_df = pd.DataFrame(box_2)
#print(type(box_2_df))
#print(box_2_df)
box_2_df.rename(columns = {0: "month"},  inplace=True)
print(box_2_df)


# 將串列合併回去
#print(type(df4[data]))

clean = pd.concat([box_1_df,box_2_df,df4[data]], axis=1)
clean.head()
#print(len(clean))
#print(clean)

#timestampStr = df4_date.to_string()
#print(timestampStr.iloc[1])
#timestamplist = list(timestampStr.split())
#print(timestamplist)


#for i in range(0,len(df4_date)):
    #dt_1 = timestampStr[0:4]
    #print(len(dt_1))
    #dt_2 = timestampStr[i][5:7].split()
    #dt_3.append(dt_1+dt_2)

    
#print(dt_3)



#df = pd.DataFrame(data, columns =['Team', 'Age', 'Score']) 
#print(df)
#a = df.pivot('Team','Age', 'Score') 
#print(a)     
    
#df4.head()
#print(df4.columns)
#df4.iloc[260:261]
#df4[data]
#df4.index
#df4.index.name = ""
#df4.set_index("date" , inplace=True)

# df4["陳時中"] = df4["陳時中"].replace(0,99) # 不是字串,不用.str

#print(len(df4.iloc[ : ]))

# 匯成JSON檔案
#preload = json.loads(df4.to_json(orient='table'))
#print(json.dumps(preload, ensure_ascii=False))


## 輸出CSV
#print(len(pList))
#print(pList_df)
#df4.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile2')


df4_date_df = pd.DataFrame(eval(df4_date))
#eval() arg 1 must be a string, bytes or code object



