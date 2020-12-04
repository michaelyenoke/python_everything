# Part Two - 整理出 mean / hot_now / diff 表格 by year

###### section 01 ######

######################
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


###### section 02 ######

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


###### section 03 ######

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
#print(clean_diff)


###### section 04 ######


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
#clean_2.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/googletrend02')


###### section 05 ######


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



###### section 06 ######


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



###### section 07 #####

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


###### section 08 ######

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


###### section 09 ######


#############################################
#在 diff 欄位中, 找出後三位 - 看出近期下降趨勢#
#############################################

#
# 先將 diff 欄位挑出來
#

# 沿用上一段計算

#
# 將 clean_2_diff 轉成 dict  
#

# 沿用上一段計算

###########
#篩選最大值#
###########


#
# 選出後 diff 順位
#


lastNum = 10  #選擇 diff 的次數
nsmallest_diff = heapq.nsmallest(lastNum,clean_2_diff_dict.values())
print(type(nsmallest_diff))



#
# for 迴圈 
# 


name_diff_down = []
year_diff_down = []



for value in nsmallest_diff:
    for key in clean_2_diff_dict.keys():
        if  clean_2_diff_dict.get(key) == value: #dict.get()取值  #print(clean_2_mean_dict['陳時中']),結果也會等於 value 
            name_diff_down.append(key)
            year_diff_down.append(value)

            
#print(type(name_diff_down))
#print(name_diff_down)
#print(type(year_diff_down))
#print(year_diff_down)


#
# 合併成一個表格
#

name_diff_down_df = pd.DataFrame(name_diff_down)   
year_diff_down_df = pd.DataFrame(year_diff_down)

down_diff_df = pd.concat([name_diff_down_df,year_diff_down_df], axis=1)
down_diff_df.columns = ['Name','下降趨勢']
print(type(down_diff_df))
print(down_diff_df)


###### section 10 ######

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

outcome_1_df.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile1999.csv')

