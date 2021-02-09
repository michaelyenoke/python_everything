#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
# https://www.python.org/dev/peps/pep-0263/

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


###############
# 取消警告設定 #
###############

warnings.filterwarnings("ignore", "Your application has authenticated using end user credentials")

#UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK. We recommend that most server applications use service accounts instead. If your application continues to use end user credentials from Cloud SDK, you might receive a "quota exceeded" or "API not enabled" error. For more information about service accounts, see https://cloud.google.com/docs/authentication/
# warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)


#############
# 記憶體設定 #
#############


#mem = virtual_memory()
#print(mem)
#np.zeros((50000,50000), dtype=np.uint8)



############################
#### Part 01 - 整理總表 #####
############################


#df=pd.read_csv('gs://openvoice_personalize/personalize_0416_itemid_renew', header=0, low_memory=False)
#print(df)

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
#print(clean)
#print(clean.columns)




########################################################
# Part 02  -  整理出 mean / hot_now / diff 表格 by year #
########################################################


#
# 計算每一個詞彙過去五年的平均 #
#


clean_group_mean_year = clean.groupby(['year']).mean()
clean_mean = clean_group_mean_year.mean()
clean_mean_2 = round(clean_mean,2)
clean_mean_2_df = pd.DataFrame(clean_mean_2)



#
# 計算 latest trend
#



clean_last_row  = clean.iloc[-1:]
clean_last_row_2 = clean_last_row[data] 
clean_last_row_2_df = clean_last_row_2.stack(0)
clean_last_row_2_df2 = clean_last_row_2_df.unstack(0)



#
# 計算 diff
#

clean_last_row_2_df2.columns = ['diff']
clean_mean_2_df.columns =['diff']
clean_diff = clean_last_row_2_df2 - clean_mean_2_df



#
# 再次組合成一個表格
#

clean_2 = pd.concat([clean_mean_2_df,clean_last_row_2_df2,clean_diff], axis = 1, sort=True)
clean_2.columns = ['mean','now_hot','diff']
clean_2.index.name = 'label'





#########################
# Part  -  匯出整理 #
#########################

#
# 如果要匯入BigQuery要將原本中文欄位取代
#


#clean.rename(columns = {'車衣': 'a01','登山車': 'a02','腳踏車': 'a03','滑步車': 'a04','公路車':'a05','折疊車':'a06','摺疊車':'a07','小徑車':'a08','淑女車':'a09','旅行車':'a10','車褲':'a11','袖套':'a12','單車':'a13','自行車':'a14','環法賽':'a15','單車環島':'a16','自行車環島':'a17','自行車安全帽':'a18','單車安全帽':'a19','腳踏車安全帽':'a20','自行車燈':'a21','腳踏車燈':'a22','自行車訓練台':'a23','單車訓練台':'a24','滑板車':'a25','長板':'a26','蛇板':'a27','滑板':'a28','BMX':'a29','越野車':'a30','環 台 公路 大賽':'a31','環台賽':'a32','防曬':'a33','反光':'a34','太陽眼鏡':'a35','墨鏡':'a36','萬眾 騎 拜':'a37','捷安特':'a38','美利達':'a39','迪卡儂':'a40','童車':'a41','兒童腳踏車':'a42','圍脖':'a43','脖圍':'a44','卡鞋':'a45','打氣筒':'a46','MTB':'a47','輔助輪':'a48','自行車手機架':'a49'},  inplace=True)

#
# 填補原本index的空白
#


#clean.set_index("year" , inplace=True)
## print(clean)


#
# 匯出成CSV
#

all_sports_csv=clean_2.to_csv().encode()
#print(table11_csv)
print('ok') 

#clean_2.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/googletrend_btw_table_01')
#print(clean_2)

#
# 匯到 gcp storage
#


client=storage.Client()
bucket=client.get_bucket('pytrendtables')
blob=bucket.blob('all_sports_csv.csv')
blob.upload_from_string(all_sports_csv)
print('ok') 


#######################
# Part  - Crontab 設定 #
#######################



# crontab -e
# * * * * * /usr/bin/python3 /home/michael_chen/deca_next_pytrend/main_nabajitest.py
# ctrl o 存檔 - https://man.linuxde.net/nano
# sudo service cron start
# sudo service cron status
