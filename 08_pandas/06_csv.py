# 先透過匯出csv再匯入的方式來處理 - 感覺不是一個好的方向

import csv
import pandas as pd
import numpy as np

dt_1 = []
dt_2 = []
dt_3 = []
dt_4 = []
dt_5 = []
dt_6 = []
empty = []

with open('csvfile2.csv', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')

    # 迴圈輸出 每一列
    for row in rows:
        empty.append(row)
        #empty.extend(row)
        #print(empty)
               
            
empty_df = pd.DataFrame(empty)        
#print(empty_df)
  #empty_df.head()
  #print(len(empty_df))
date_value = empty_df[0][0:262]
  #date_value_df = pd.DataFrame(date_value)   
print(date_value)
  #print((date_value[1][5:7]))
  #print(type(date_value[1]))
  #print(len(empty)) 262
  #print(len(empty_df)) 262


#先處理日期部分,將年與月拆分出來

for i in range(0,len(empty_df)): #取1已經拿掉表頭
    dt_1 = date_value[i][0:4].split()
    dt_2 = date_value[i][5:7].split()
    dt_3.append(dt_1+dt_2)

#print(type(dt_3))
dt_3_df = pd.DataFrame(dt_3)
#print(type(dt_3_df))
#print(dt_3_df)

    
#再將其他部分合併進來    
#寫個迴圈改善

df_kk = empty_df[1]
df_kk_df = pd.DataFrame(df_kk)

df_kk_2 = empty_df[2]
df_kk_df_2 = pd.DataFrame(df_kk_2)

df_kk_3 = empty_df[3]
df_kk_df_3 = pd.DataFrame(df_kk_3)

df_kk_4 = empty_df[4]
df_kk_df_4 = pd.DataFrame(df_kk_4)

df_kk_5 = empty_df[5]
df_kk_df_5 = pd.DataFrame(df_kk_5)

df_kk_6 = empty_df[6]
df_kk_df_6 = pd.DataFrame(df_kk_6)

df_kk_7 = empty_df[7]
df_kk_df_7 = pd.DataFrame(df_kk_7)

df_kk_8 = empty_df[8]
df_kk_df_8 = pd.DataFrame(df_kk_8)


frames = [dt_3_df, df_kk_df,df_kk_df_2,df_kk_df_3,df_kk_df_4,df_kk_df_5,df_kk_df_6,df_kk_df_7,df_kk_df_8]
result = pd.concat(frames, axis=1)
print(result)
#print(type(result))
#result.head()
#result.tail()

result[np.negative(pd.Series(result.columns).str.contains('index'))]
#dt_1 = pd.DataFrame(dt_1)
#result.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile3')
