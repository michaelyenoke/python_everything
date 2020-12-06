from pytrends.request import TrendReq
from pprint import pprint
from time import sleep
from datetime import datetime # import datetime classs from datetime module
import pandas as pd
import json
import csv
import matplotlib.pyplot as plt
from numpy.random import randn # 生成隨機數
import heapq

data = ['陳時中','環島','獨輪車','登山車','火車','梨泰院','新冠','新垣結衣','想見你','迪卡儂','武漢','佐藤健']


pList = []


for keywords in data:
    keywords_list = [keywords]
    pytrend = TrendReq(hl='en-US', tz=360)
    pytrend.build_payload(keywords_list, cat=0, timeframe='today 5-y', geo='TW', gprop='')
    interest_over_time_df = pytrend.interest_over_time()[keywords]
    pList.append(interest_over_time_df)
pList_df = pd.DataFrame(pList)


# 欄與列的整理
df3 = pList_df.stack(0)
df4 = df3.unstack(0)
# 將index.name的date改成column
df4.reset_index(inplace=True)

print(df4)


d = []

#
# 將日期單獨抽離出來,格式 timeframe
#


df4_date = df4['date']


for i in range(0,len(df4)):
    # 將timeframe 轉換成 datetime
    date_time_obj = datetime.strptime(str(df4_date[i]), '%Y-%m-%d %H:%M:%S') 
    # 將 datetime 轉換成 string, 並拆開
    d.append(date_time_obj.strftime("%Y,%m").split())
    

print(d)

box_1 = []
box_2 = []


for j in range(0,len(d)):
    d_sp = d[j][0].split(",",1)
    d_sp_y = d_sp[0]
    d_sp_m = d_sp[1]
    box_1.append(d_sp_y)
    box_2.append(d_sp_m)
    #print(type(d_sp))


box_1_df = pd.DataFrame(box_1)
box_1_df.rename(columns = {0: "year"},  inplace=True)
box_2_df = pd.DataFrame(box_2)
box_2_df.rename(columns = {0: "month"},  inplace=True)

print(box_2_df)

print(box_1_df)

clean = pd.concat([box_1_df,box_2_df,df4[data]], axis=1)

print(clean)


