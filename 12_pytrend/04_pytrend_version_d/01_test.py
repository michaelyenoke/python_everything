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




#############################
#### Part One - 整理總表 #####
#############################


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



##################################################
# Part Two -  將日期(年,月)單獨抽離出來並與重新合併 #
##################################################


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



########################################################
# Part Three - 整理出 mean / hot_now / diff 表格 by year#
########################################################



clean_group_mean_year = clean.groupby(['year']).mean()
clean_mean = clean_group_mean_year.mean()
clean_mean_2 = round(clean_mean,2)
clean_mean_2_df = pd.DataFrame(clean_mean_2)



clean_last_row  = clean.iloc[-1:]
clean_last_row_2 = clean_last_row[data] # 去掉前面的 year, month
clean_last_row_2_df = clean_last_row_2.stack(0)
clean_last_row_2_df2 = clean_last_row_2_df.unstack(0)
clean_last_row_2_df2.columns = ['diff']
clean_mean_2_df.columns =['diff']
clean_diff = clean_last_row_2_df2 - clean_mean_2_df


clean_2 = pd.concat([clean_mean_2_df,clean_last_row_2_df2,clean_diff], axis=1)
clean_2.columns = ['mean','now_hot','diff']




##########################################
# 在 mean 欄位中, 找出前N位 - 看出長期熱銷#
##########################################


clean_2_mean = clean_2['mean']
clean_2_mean_dict = dict(clean_2_mean) 
clean_2_mean_dict_v = clean_2_mean_dict.values() # 取出 dict 的 值
clean_2_mean_dict_k = clean_2_mean_dict.keys()   # 取出 dict 的 鍵


topNum = 3  #選擇top的次數
nlargestList = heapq.nlargest(topNum,clean_2_mean_dict.values())


top_name = []
year_mean = []


for value in nlargestList:
    for key in clean_2_mean_dict.keys():
        if  clean_2_mean_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            top_name.append(key)
            year_mean.append(value)


top_name_df = pd.DataFrame(top_name)   
year_mean_df = pd.DataFrame(year_mean)
      
    
top_mean_df = pd.concat([top_name_df,year_mean_df], axis=1)
top_mean_df.columns = ['Name','5年平均']


#############################################
# 在 now_hot 欄位中, 找出前N位 - 看出近期熱銷#
############################################


clean_2_now_hot = clean_2['now_hot']
clean_2_now_hot_dict = dict(clean_2_now_hot) 
clean_2_now_hot_dict_v = clean_2_now_hot_dict.values() # 取出 dict 的 值
clean_2_now_hot_dict_k = clean_2_now_hot_dict.keys()   # 取出 dict 的 鍵


topNum = 3  #選擇top的次數
nlargestList_now_hot = heapq.nlargest(topNum,clean_2_now_hot_dict.values())


now_hot_top_name = []
now_hot_num = []


for value in nlargestList_now_hot:
    for key in clean_2_now_hot_dict.keys():
        if  clean_2_now_hot_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            now_hot_top_name.append(key)
            now_hot_num.append(value)



now_hot_top_name_df = pd.DataFrame(now_hot_top_name)   
now_hot_num_df = pd.DataFrame(now_hot_num) 
now_hot_df = pd.concat([now_hot_top_name_df,now_hot_num_df], axis=1)
now_hot_df.columns = ['Name','目前熱搜']



############################################
# 在 diff 欄位中, 找出前N位 - 看出近期上升趨勢#
############################################


clean_2_diff = clean_2['diff']
clean_2_diff_dict = dict(clean_2_diff) 
clean_2_diff_dict_v = clean_2_diff_dict.values() # 取出 dict 的 值
clean_2_diff_dict_k = clean_2_diff_dict.keys()   # 取出 dict 的 鍵


topNum = 3  #選擇top的次數
nlargestList_diff = heapq.nlargest(topNum,clean_2_diff_dict.values())


top_name_diff = []
year_diff = []


for value in nlargestList_diff:
    for key in clean_2_diff_dict.keys():
        if  clean_2_diff_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            top_name_diff.append(key)
            year_diff.append(value)



top_name_diff_df = pd.DataFrame(top_name_diff)   
year_diff_df = pd.DataFrame(year_diff)


top_diff_df = pd.concat([top_name_diff_df,year_diff_df], axis=1)
top_diff_df.columns = ['Name','上升趨勢']




###########################################
#在 diff 欄位中, 找出後N位 - 看出近期下降趨勢#
###########################################



lastNum = 3  
nsmallest_diff = heapq.nsmallest(lastNum,clean_2_diff_dict.values())


name_diff_down = []
year_diff_down = []



for value in nsmallest_diff:
    for key in clean_2_diff_dict.keys():
        if  clean_2_diff_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            name_diff_down.append(key)
            year_diff_down.append(value)


name_diff_down_df = pd.DataFrame(name_diff_down)   
year_diff_down_df = pd.DataFrame(year_diff_down)

down_diff_df = pd.concat([name_diff_down_df,year_diff_down_df], axis=1)
down_diff_df.columns = ['Name','下降趨勢']




######################################
#合併 四個 DataFrame 成為一個 DataFram#
######################################

outcome_1 = []
outcome_df = [now_hot_df,top_mean_df,top_diff_df,down_diff_df]


for out in range(0,len(outcome_df)):
    outcome_1.append(outcome_df[out])
    
    
print(clean_2)
print(outcome_1)

