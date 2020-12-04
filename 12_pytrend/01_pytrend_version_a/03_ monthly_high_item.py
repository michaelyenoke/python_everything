###### section 01 #####

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


###### section 02 ######

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


###### section 03 ######

    
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


###### section 04 #####

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



######  section 05 #####


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






 




