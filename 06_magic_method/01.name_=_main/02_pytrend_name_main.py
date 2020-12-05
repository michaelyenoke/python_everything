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
import heapq
import os
import gcsfs
import pandas as pd
from google.cloud import storage
import numpy as np
from psutil import virtual_memory
import warnings 

#class01類別- pytrend - 包含所有pytrend的function

#class02類別-


def pytrend_api_func01(data): #第一個function用來抓pytrend的資料
    #Section_1_pytrend_api
    pList = []
    for keywords in data:
        keywords_list = [keywords]
        pytrend = TrendReq(hl='en-US', tz=360)
        pytrend.build_payload(keywords_list, cat=0, timeframe='today 5-y', geo='TW', gprop='')
        interest_over_time_df = pytrend.interest_over_time()[keywords]
        pList.append(interest_over_time_df)
    pList_df = pd.DataFrame(pList)
    df3 = pList_df.stack(0)
    df4 = df3.unstack(0)
    df4.reset_index(inplace=True)
    return df4
    
 btw = ['車衣','登山車','腳踏車','滑步車','公路車','折疊車','摺疊車','小徑車','淑女車','旅行車','車褲','袖套','單車','自行車','環法賽','單車環島','自行車環島','自行車安全帽','單車安全帽','腳踏車安全帽','自行車燈','腳踏車燈','自行車訓練台','單車訓練台','滑板車','長板','蛇板','滑板','BMX','越野車','環 台 公路 大賽','環台賽','防曬','反光','太陽眼鏡','墨鏡','萬眾 騎 拜','捷安特','美利達','迪卡儂','童車','兒童腳踏車','圍脖','脖圍','卡鞋','打氣筒','MTB','輔助輪','自行車手機架']
 
 pytrend_api_func01(btw)
 
 ans01 = pytrend_api_func01(btw)
 
 print(ans01)
 
 
 def pytrend_clean():     #funciton etl 將日期分開成為 年和月
    #Section_2_seperate_month_year
    d = []
    df4_date = df4['date']
    for i in range(0,len(df4)):
        date_time_obj = datetime.strptime(str(df4_date[i]), '%Y-%m-%d %H:%M:%S') 
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
    
  
ans01.pytrend_clean()

supwater = ['sup','sup 體驗','Stand Up Paddle','立式划槳','立槳衝浪','立槳','kayak','獨木舟','救生衣','溯溪鞋','防滑鞋','膠鞋','更衣帳']

def pytrend_5year_mean_2():  #function - 計算5年的中位數
    #Section_3_five_year_average 
    clean_group_mean_year = clean.groupby(['year']).mean()
    clean_mean = clean_group_mean_year.mean()
    clean_mean_2 = round(clean_mean,2)
    clean_mean_2_df = pd.DataFrame(clean_mean_2)
    
def pytrend_hot_now(): #function - 抓表格的最後一行
    #Section_4_hot_now
    clean_last_row  = clean.iloc[-1:]
    clean_last_row_2 = clean_last_row[data] 
    clean_last_row_2_df = clean_last_row_2.stack(0)
    clean_last_row_2_df2 = clean_last_row_2_df.unstack(0)
    
def pytrend_diff(): #function - 計算兩個表格之差
    #Section_5_diff
    clean_last_row_2_df2.columns = ['diff']
    clean_mean_2_df.columns =['diff']
    clean_diff = clean_last_row_2_df2 - clean_mean_2_df
    
    
def combine():  #function - 將個別資料合併成一個表格的function    
    #Section_6_Table_combine
    clean_2 = pd.concat([clean_mean_2_df,clean_last_row_2_df2,clean_diff], axis=1)
    clean_2.columns = ['mean','now_hot','diff']
    clean_2.index.name = 'label'
    #Section_7_To_Csv 
    clean3_csv=clean_2.to_csv().encode()  
    #print('ok')
    #print(clean_2)
    #print(clean3_csv)
    
 supwater = ['sup','sup 體驗','Stand Up Paddle','立式划槳','立槳衝浪','立槳','kayak','獨木舟','救生衣','溯溪鞋','防滑鞋','膠鞋','更衣帳']

if pytrend_api_func01(supwater):
    df4.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/googletrend01')
    
 def gcp_strorage(data): # fuction gcp 相關功能
    client=storage.Client()
    bucket=client.get_bucket('pytrendtables')
    blob=bucket.blob('data_csv.csv')
    blob.upload_from_string(data_csv)
    print('ok') 
 
nabaiji = ['游泳','武漢 肺炎 游泳','泳鏡','蛙鏡','防霧','毛巾','浴巾','泳衣','泳裝','泳褲','比基尼','泳圈','防水包','防水袋','戲水','鼻夾','耳塞','划手板','自由潛水','水中有氧','泳池','仰泳','蛙式','自由式','蛙泳','玩水','冬泳','蝶泳','蛙鞋']


if __name__ == '__main__':
    main()
 

