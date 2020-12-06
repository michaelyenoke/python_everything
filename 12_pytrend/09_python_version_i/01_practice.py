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
import os
import gcsfs
import pandas as pd
from google.cloud import storage
import numpy as np
from psutil import virtual_memory
import warnings  


data = ['籃球','登山','健行','攀岩','自行車','游泳','戲水','潛水','衝浪','龍舟','划船','慢跑','馬拉松','蛇板','滑板','滑板車','高爾夫','溜冰','滑雪','瑜珈','皮拉提斯','有氧','排球','壁球','網球','足球','重量訓練','重訓','浮潛','釣魚','立槳','射箭','滾球','狩獵','馬術','鐵人','航海','健走','羽球','羽毛球','桌球','飛鏢','曲棍球','橄欖球','棒球','拳擊','露營','跑步','舞蹈','健身','撞球','爬山']


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



#
# 將日期(年,月)單獨抽離出來並與重新合併 #
#


d = []

df4_date = df4['date']


for i in range(0,len(df4)):
    # 將timeframe 轉換成 datetime
    date_time_obj = datetime.strptime(str(df4_date[i]), '%Y-%m-%d %H:%M:%S') 
    # 將 datetime 轉換成 string, 並拆開
    d.append(date_time_obj.strftime("%Y,%m").split())


box_1 = []
box_2 = []

for j in range(0,len(d)):
    d_sp = d[j][0].split(",",1)
    d_sp_y = d_sp[0]
    d_sp_m = d_sp[1]
    box_1.append(d_sp_y)
    box_2.append(d_sp_m)


box_1_df = pd.DataFrame(box_1)
box_1_df.rename(columns = {0: "year"},  inplace=True)
box_2_df = pd.DataFrame(box_2)
box_2_df.rename(columns = {0: "month"},  inplace=True)


clean = pd.concat([box_1_df,box_2_df,df4[data]], axis=1)
print(clean)
