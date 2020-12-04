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


########## section 01 ##########

data = ['車衣','登山車','腳踏車','滑步車','公路車','折疊車','摺疊車','小徑車','淑女車','旅行車','車褲','袖套','單車','自行車','環法賽','單車環島','自行車環島','自行車安全帽','單車安全帽','腳踏車安全帽','自行車燈','腳踏車燈','自行車訓練台','單車訓練台','滑板車','長板','蛇板','滑板','BMX','越野車','環 台 公路 大賽','環台賽','防曬','反光','太陽眼鏡','墨鏡','萬眾 騎 拜','捷安特','美利達','迪卡儂','童車','兒童腳踏車','圍脖','脖圍','卡鞋','打氣筒','MTB','輔助輪','自行車手機架']
#有些詞彙沒有搜尋熱度 - 暫不處理 '男性自行車','武漢肺炎','女性自行車','男性自行車','愛的迫降'
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
#df4.head()
print(df4)
#print(type(df4))

# 輸出csv
#df4.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/googletrend01')



########## section 02 ##########


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


########## section 03 ##########

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



########## section 04 ##########

#如果要匯到bigquery將欄位名稱從中文換掉
#clean.rename(columns = {'車衣': 'a01','登山車': 'a02','腳踏車': 'a03','滑步車': 'a04','公路車':'a05','折疊車':'a06','摺疊車':'a07','小徑車':'a08','淑女車':'a09','旅行車':'a10','車褲':'a11','袖套':'a12','單車':'a13','自行車':'a14','環法賽':'a15','單車環島':'a16','自行車環島':'a17','自行車安全帽':'a18','單車安全帽':'a19','腳踏車安全帽':'a20','自行車燈':'a21','腳踏車燈':'a22','自行車訓練台':'a23','單車訓練台':'a24','滑板車':'a25','長板':'a26','蛇板':'a27','滑板':'a28','BMX':'a29','越野車':'a30','環 台 公路 大賽':'a31','環台賽':'a32','防曬':'a33','反光':'a34','太陽眼鏡':'a35','墨鏡':'a36','萬眾 騎 拜':'a37','捷安特':'a38','美利達':'a39','迪卡儂':'a40','童車':'a41','兒童腳踏車':'a42','圍脖':'a43','脖圍':'a44','卡鞋':'a45','打氣筒':'a46','MTB':'a47','輔助輪':'a48','自行車手機架':'a49'},  inplace=True)
#clean.set_index("year" , inplace=True)
#print(clean)

#table10_csv=clean.to_csv().encode()
#print(table10_csv)

#clean.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/googletrend_nabaji_04')


