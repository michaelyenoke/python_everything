spread sheet
https://docs.google.com/spreadsheets/d/17tBkLeYHb3ZU4dn8Cfuvyk2WE-mb5hZR2jTTKliPDDQ/edit#gid=0

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


# Part One - 整理總表

data = ['游泳','武漢 肺炎 游泳','泳鏡','蛙鏡','防霧','毛巾','浴巾','泳衣','泳裝','泳褲','比基尼','泳圈','防水包','防水袋','戲水','鼻夾','耳塞','划手板','自由潛水','水中有氧','泳池','仰泳','蛙式','自由式','蛙泳','玩水','冬泳','蝶泳','蛙鞋']
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
#df4.head()
print(df4)
#print(type(df4))

# 輸出csv
df4.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/googletrend_nabaji_01')


############################################################
# 將日期(年,月)單獨抽離出來並從 timeframe - datetime - string#
############################################################


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
    d.append(date_time_obj.strftime("%Y,%m").split())
    #print(type(d))

#print(d)
#print(d[0][0])
#print(type(d[0][0]))

############################################
#將年月分開成為兩筆資料,之後再將所有資料接回去#
############################################



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
#print(box_2_df)


#
# 將串列合併回去
#

#print(type(df4[data]))

clean = pd.concat([box_1_df,box_2_df,df4[data]], axis=1)
#clean.head()
#print(len(clean))
print(type(clean))
print(clean)

# Part Two - 整理出 mean / hot_now / diff 表格 by year

#######################
#每個名詞計算五年的平均#
######################
# 還是需要先 group by year; 再計算出 
# 再用 今年的平均去減去年的平均

clean_group_mean_year = clean.groupby(['year']).mean()
#print(clean_group_mean_year)
#print(type(clean)) # DataFrame

# 要計算平均之前,要先把年月拿掉 - 得到過去五年的總平均 past_avg_5y

clean_mean = clean_group_mean_year.mean()
#print(clean_mean)
#print(type(clean_mean))
clean_mean_2 = round(clean_mean,2)

#print(clean_mean_2)
clean_mean_2_df = pd.DataFrame(clean_mean_2)
#print(type(clean_mean_2_df))
print(clean_mean_2_df)

##############################
# 計算最後一個的趨勢 Trend_Now##
##############################

clean_last_row  = clean.iloc[-1:]
#print(clean_last_row)
#print(type(clean_last_row))


clean_last_row_2 = clean_last_row[data] # 去掉前面的 year, month
#print(clean_last_row_2)



clean_last_row_2_df = clean_last_row_2.stack(0)
clean_last_row_2_df2 = clean_last_row_2_df.unstack(0)
print(clean_last_row_2_df2)
#print(type(clean_last_row_2_df2))

###########
#計算diff#
##########
#print(clean_last_row_2_df2)
#print(type(clean_last_row_2_df2))
#print(clean_mean_2_df)
#print(type(clean_mean_2_df))

clean_last_row_2_df2.columns = ['diff']
clean_mean_2_df.columns =['diff']


clean_diff = clean_last_row_2_df2 - clean_mean_2_df
print(clean_diff)


##################
#再次組合成一個表格#
##################

clean_2 = pd.concat([clean_mean_2_df,clean_last_row_2_df2,clean_diff], axis=1)
#print(clean_2)
#print(type(clean_2))
# 給欄位命名
clean_2.columns = ['mean','now_hot','diff']
#print(clean_2)
print(clean_2)
clean_2.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/googletrend_nabaji_02')

##########################################
# 在 mean 欄位中, 找出前三位 - 看出長期熱銷#
##########################################

#
#先將 mean 欄位挑出來
#

clean_2_mean = clean_2['mean']

#print(clean_2_mean)

#
# 將 clean_2_mean 轉成 dict
#


clean_2_mean_dict = dict(clean_2_mean) 
#print(type(clean_2_mean_dict))
#print(clean_2_mean_dict)
clean_2_mean_dict_v = clean_2_mean_dict.values() # 取出 dict 的 值
#print(clean_2_mean_dict.values())
clean_2_mean_dict_k = clean_2_mean_dict.keys()   # 取出 dict 的 鍵
#print(clean_2_mean_dict.keys())


###########
#篩選最大值#
###########


topNum = 10  #選擇top的次數
nlargestList = heapq.nlargest(topNum,clean_2_mean_dict.values())
#print(nlargestList)

top_name = []
year_mean = []


#
# for 迴圈 
#


for value in nlargestList:
    for key in clean_2_mean_dict.keys():
        if  clean_2_mean_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            top_name.append(key)
            year_mean.append(value)

            
#print(type(top_name))
#print(type(year_mean))

    
#
# 合併成一個表格
#    

top_name_df = pd.DataFrame(top_name)   
year_mean_df = pd.DataFrame(year_mean)
      
    
top_mean_df = pd.concat([top_name_df,year_mean_df], axis=1)
top_mean_df.columns = ['Name','5年平均']
#print(type(top_mean_df))
print(top_mean_df)  

#############################################
# 在 now_hot 欄位中, 找出前三位 - 看出近期熱銷#
############################################

#
#先將 now_hot 欄位挑出來
#

clean_2_now_hot = clean_2['now_hot']
#print(clean_2_now_hot)


#
# 將 clean_2_now_hot 轉成 dict
#


clean_2_now_hot_dict = dict(clean_2_now_hot) 
#print(type(clean_2_now_hot_dict))
#print(clean_2_now_hot_dict)
clean_2_now_hot_dict_v = clean_2_now_hot_dict.values() # 取出 dict 的 值
#print(clean_2_now_hot_dict.values())
clean_2_now_hot_dict_k = clean_2_now_hot_dict.keys()   # 取出 dict 的 鍵
#print(clean_2_now_hot_dict.keys())


###########
#篩選最大值#
###########


topNum = 10  #選擇top的次數
nlargestList_now_hot = heapq.nlargest(topNum,clean_2_now_hot_dict.values())
#print(nlargestList)


#
# for 迴圈 
# 


now_hot_top_name = []
now_hot_num = []


for value in nlargestList_now_hot:
    for key in clean_2_now_hot_dict.keys():
        if  clean_2_now_hot_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            now_hot_top_name.append(key)
            now_hot_num.append(value)

            
            
#print(type(now_hot_top_name))
#print(now_hot_top_name)
#print(type(now_hot_num))
#print(now_hot_num)




#
# 合併成一個表格
#    


now_hot_top_name_df = pd.DataFrame(now_hot_top_name)   
now_hot_num_df = pd.DataFrame(now_hot_num)
      
    
now_hot_df = pd.concat([now_hot_top_name_df,now_hot_num_df], axis=1)
now_hot_df.columns = ['Name','目前熱搜']
#print(type(now_hot_df))
print(now_hot_df)


##############################################
# 在 diff 欄位中, 找出前三位 - 看出近期上升趨勢#
##############################################

#
# 先將 diff 欄位挑出來
#


clean_2_diff = clean_2['diff']
#print(clean_2_diff)



#
# 將 clean_2_diff 轉成 dict  
#


clean_2_diff_dict = dict(clean_2_diff) 
#print(type(clean_2_diff_dict))
#print(clean_2_diff_dict)
clean_2_diff_dict_v = clean_2_diff_dict.values() # 取出 dict 的 值
#print(clean_2_diff_dict.values())
clean_2_diff_dict_k = clean_2_diff_dict.keys()   # 取出 dict 的 鍵
#print(clean_2_diff_dict.keys())


###########
#篩選最大值#
###########

#
# 選出前 top 順位
#


topNum = 10  #選擇top的次數
nlargestList_diff = heapq.nlargest(topNum,clean_2_diff_dict.values())
#print(nlargestList_diff)


#
# for 迴圈 
# 


top_name_diff = []
year_diff = []

for value in nlargestList_diff:
    for key in clean_2_diff_dict.keys():
        if  clean_2_diff_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            top_name_diff.append(key)
            year_diff.append(value)

#print(type(top_name_diff))
#print(top_name_diff)
#print(type(year_diff))
#print(year_diff)



#
# 合併成一個表格
#

top_name_diff_df = pd.DataFrame(top_name_diff)   
year_diff_df = pd.DataFrame(year_diff)

top_diff_df = pd.concat([top_name_diff_df,year_diff_df], axis=1)
top_diff_df.columns = ['Name','上升趨勢']
print(type(top_diff_df))
print(top_diff_df)

######################################
#合併 四個 DataFrame 成為一個 DataFram#
######################################

outcome_1 = []

outcome_df = [now_hot_df,top_mean_df,top_diff_df,down_diff_df]
#print(outcome_df)
#print(len(outcome_df))


for out in range(0,len(outcome_df)):
    outcome_1.append(outcome_df[out])

print(type(outcome_1))    
print(outcome_1)

# 輸出csv

outcome_1_df = pd.DataFrame(outcome_1)   

#outcome_1_df.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile1999.csv')


# Part Three : Monthly High Item

###############################
#按月去分析 - 每個月分最高 mean#
###############################


#
# 按月找出平均數 group by month
#


#print(clean)
clean_group_mean_month = clean.groupby(['month']).mean()
#print(clean_group_mean_month)



#
# 調整表頭
#



clean_group_mean_month_01 = []
clean_group_mean_month_02 = []


clean_group_mean_month_01 = clean_group_mean_month.stack(0)
clean_group_mean_month_02 = clean_group_mean_month_01.unstack(0)



#clean_group_mean_month_02.head(15)
#print(len(clean_group_mean_month_02)) #11
print(type(clean_group_mean_month_02))


months = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
clean_group_mean_month_02.columns = [months]
print(clean_group_mean_month_02)


#
# 01 先看每個月最高的三個詞
#


mon_column = []

l = len(clean_group_mean_month_02)
#print(l)
#print(clean_group_mean_month_02.iloc[0:12,1])


for n in range(0,l):
    mon_column.append(clean_group_mean_month_02.iloc[0:l,n])
    
#print(mon_column)

mon_column_df = pd.DataFrame(mon_column)
mon_column_df_round = round(mon_column_df,2)
#print(mon_column_df_round)


#
# 先找出個別欄位的前三名
#

top_mon_nlargest = []

for w in range(0,12):
    yy = mon_column_df.iloc[w] 
    top_mon_nlargest.append(heapq.nlargest(3, yy))

    
top_mon_nlargest_df = pd.DataFrame(top_mon_nlargest)
top_mon_nlargest_df = round(top_mon_nlargest_df,2)
print(top_mon_nlargest_df)


# 改成選擇當前月份 和 +1 , -1 


#
# 前一個月份
#

x = datetime.now()
b_01 = x.month - 2



kk = top_mon_nlargest_df.loc[b_01] # 0~11

kk_dict = dict(kk)
kk_v = kk_dict.values()

gg = mon_column_df_round.iloc[b_01]
gg_dict = dict(gg)
gg_dict_v = gg_dict.values()
gg_dict_k = gg_dict.keys()

month_top_1 = []
month_top_2 = [] 

for v in kk_v:
    for k in gg_dict_k:             
        if  gg_dict[k] == v: 
            month_top_1.append(k)
            month_top_2.append(v)
#print(month_top_1)  
#print(month_top_2)

                
month_top_1_df = pd.DataFrame(month_top_1)
month_top_2_df = pd.DataFrame(month_top_2)

month_top_df = pd.concat([month_top_1_df,month_top_2_df], axis=1)
month_top_df.columns = ['Name','累績月分最高(上月)']
print(month_top_df)
    



#
# 當前月份
#


x = datetime.now()
b_02 = x.month - 1



kk = top_mon_nlargest_df.loc[b_02] # 0~11

kk_dict = dict(kk)
kk_v = kk_dict.values()

gg = mon_column_df_round.iloc[b_02]
gg_dict = dict(gg)
gg_dict_v = gg_dict.values()
gg_dict_k = gg_dict.keys()

month_top_1 = []
month_top_2 = [] 

for v in kk_v:
    for k in gg_dict_k:             
        if  gg_dict[k] == v: 
            month_top_1.append(k)
            month_top_2.append(v)
#print(month_top_1)  
#print(month_top_2)

                
month_top_1_df = pd.DataFrame(month_top_1)
month_top_2_df = pd.DataFrame(month_top_2)

month_top_df = pd.concat([month_top_1_df,month_top_2_df], axis=1)
month_top_df.columns = ['Name','(累積)月分最高(本月)']
print(month_top_df)
    

    
    
#
# 下個月份
#



x = datetime.now()
b_03 = x.month 



kk = top_mon_nlargest_df.loc[b_03] # 0~11

kk_dict = dict(kk)
kk_v = kk_dict.values()

gg = mon_column_df_round.iloc[b_03]
gg_dict = dict(gg)
gg_dict_v = gg_dict.values()
gg_dict_k = gg_dict.keys()

month_top_1 = []
month_top_2 = [] 

for v in kk_v:
    for k in gg_dict_k:             
        if  gg_dict[k] == v: 
            month_top_1.append(k)
            month_top_2.append(v)
#print(month_top_1)  
#print(month_top_2)

                
month_top_1_df = pd.DataFrame(month_top_1)
month_top_2_df = pd.DataFrame(month_top_2)

month_top_df = pd.concat([month_top_1_df,month_top_2_df], axis=1)
month_top_df.columns = ['Name','(累積)月分最高(下月)']
print(month_top_df)

#
# 02 再先找出每個詞最高的三個月份 --- 
#

clean_group_mean_month_02.iloc[1]
o = list(clean_group_mean_month_02.iloc[1])
#print(o)

dict_mon_num = dict(zip(months,o))
#print(dict_mon_num['Jan']) # dict {'Jan':xxxx, }

uu_dict_top = []
uu_dict_top_v = []


for c in range(0,len(data)):
    for z in uu_dict_top:
        for h in months:
            uu = list(clean_group_mean_month_02.iloc[c]) 
            uu_dict_v = uu_dict.values()
            uu_dict_top.extend(heapq.nlargest(3, uu_dict_v)) # type:list
            print(uu_dict_top)
            #if dict_mon_num[h] == z: 
                #uu_dict_top_v.append(dict(h,z))


# Part Four : Line Bot & Send Email with google sheet

##########
#Line Bot#
##########


#############
#寄送電子郵件#
#############

import smtplib

#mySMTP = smtplib.SMTP('smtp.gmail.com',587)
#print(type(mySMTP))
#mySMTP.ehlo() # 250 代表成功,啟動伺服器對話
#mySMTP.starttls() # 220 代表成功,告知郵件伺服器郵件加密

#mySMTP.login('michaelyenoke@gmail.com','2ouiougi')


s = smtplib.SMTP('smtplib.gmail.com',587)
s.ehlo()
s.starttls()
s.login('michaelyenoke@gmail.com','zaleoc2ouiougi')
try:
    s.sendmail('michaelyenoke@gmail.com','michaelyenoke@hotmail.com','message_hihi')
except:
    print (failed)
    
 

# Part Five : Predict

"""
1. Like Roy Case - 合併起來做一個更大的模型 - 加入會員交易與GA交易資料 - 以門店與電商作為個人來推薦
2. 建立商品預測模型 - 最後比照 Clair 關鍵字 ; Roy 商品名單 - 刪除不在上面的東西
"""

# Part Six : 網路爬蟲與網路聲量模型 - 產出新的關鍵字

mon_column_large_dict = []

for i in range(0,11):
    mon_column_large_dict.append(dict(mon_column_large[i]))
    

    
print(mon_column_large_dict)

#
# 轉成字典後,再將值與鍵合併
#


#clean_group_mean_month_02_dict = dict(clean_group_mean_month_02) 
#print(type(clean_group_mean_month_02_dict))
#print(clean_group_mean_month_02_dict)
#print(clean_group_mean_month_02_dict.values()) 
#print(clean_group_mean_month_02_dict.keys()) 
#mon_column_larg_dict_k = mon_column_larg_dict.keys()   # 取出 dict 的 鍵
#print(mon_column_larg_dict_k)


#name_diff = []
#year_diff_down = []



#for value in nsmallest_diff:
#    for key in clean_2_diff_dict.keys():
#        if  clean_2_diff_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
#            name_diff_down.append(key)
#            year_diff_down.append(value)


    
    
# 先將月份選出來

#print(clean_group_mean_month_02.loc[1])


#for mon in months:
#    print(clean_group_mean_month_02[mon])


#
# 將 month_01 轉成 dict  
#


month_dict = dict(month_01) 
#print(type(month_01_dict))
#print(month_01_dict)
month_01_dict_v = month_01_dict.values() # 取出 dict 的 值
#print(clean_2_diff_dict.values())
month_01_dict_k = month_01_dict.keys()   # 取出 dict 的 鍵
#print(clean_2_diff_dict.keys())


###########
#篩選最大值#
###########


#
# 選出前 top 順位
#


topNum = 3  #選擇top的次數
nlargestList_month= heapq.nlargest(topNum,month_01_dict.values())
#print(nlargestList_month_01)


#
# for 迴圈 
# 


month_name = []
month_high = []

for value in nlargestList_month:
    for key in month_01_dict.keys():
        if  month_01_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            month_01.append(key)
            month_high.append(value)

            
            
print(type(top_name_diff))
print(top_name_diff)
print(type(year_diff))
print(year_diff)


import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 24, 37, 2]

# 最大的3个数的索引
max_num_index_list = map(nums.index, heapq.nlargest(3, nums))

# 最小的3个数的索引
min_num_index_list = map(nums.index, heapq.nsmallest(3, nums))

print(list(max_num_index_list))
print(list(min_num_index_list))

###########
# ????????#
###########

#能否透過pytrend直接抓取熱門關鍵字


##############################
#Wiki Pedia Bigquery Opendata#
##############################




