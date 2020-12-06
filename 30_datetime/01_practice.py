from datetime import datetime
import pandas as pd

df=pd.read_csv('file:///C:/Users/MichaelCHEN/Desktop/2020S1%20Product%20review%20detail.csv', encoding='big5', names=['user', 'like', 'suggest', 'age', 'gender', 'd_t'], parse_dates=["d_t"])
#print(type(df.d_t)) # Series
print(df.d_t)

#k=df.d_t
#print(k.microsecond)
#dt = datetime.now()     
#dt.microsecond
#print(type(datetime.now()))

#kdt = pd.to_datetime(k, errors='coerce')
#print(kdt.microsecond)
#print(type(kdt))

import csv
import time
from datetime import datetime

with open('C:/Users/MichaelCHEN/Desktop/2020S1 Product review detail.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  
 
  # 以迴圈輸出每一列
  for row in rows:
    box = []
    box.append(row[5])
    yy = box[0]    
    #print(type(yy)) #str
    yy_split = yy.split()
    #print(yy_split)        
    #print(yy_split[0])
    yy_date = yy_split[0]
    year_count = yy_date[0:4]
    month_count = yy_date[5:7]
    print(month_count)
    #print(yy_date)
    #print(yy_split[1])
    yy_time = yy_split[1]
    #print(yy_time)
    
    #應該以日期相減,月日相減部分比較難計算
    #((year_count-1970)*365*86400)+()
    
    
    #datetime_object = datetime.strptime(yy,'%Y-%m-%d %H:%M:%S')        
    #print(datetime_object)
    #print(type(datetime_object)) #datetime
    #yy_datetime = int(time.mktime(time.strptime(datetime_object))) - time.timezone
    #print(yy_datetime)
    #print(type(datetime_object))
    #print(datetime_object)
    #ydt = datetime_object.microsecond
    #print(ydt)
    
dt=datetime.now()
dt_epoch = dt.microsecond
print(dt_epoch)

"""
s = "Hello OutOfMemory.CN"
small = s[2:4]
print(small)

import datetime
datetime.datetime.fromtimestamp(1586854774).isoformat()

import time
int(time.mktime(time.strptime("2020-04-14 10:59:34"))) - time.timezone

https://stackoverflow.com/questions/466345/converting-string-into-datetime

df=pd.read_csv("filename.csv" , parse_dates=["<column name>"])
type(df.<column name>)

https://github.com/tomlinNTUB/Python/blob/master/pandas/%E8%AE%80%E5%8F%96%E6%AC%84%E4%BD%8D%E5%88%86%E9%9B%A2%E8%B3%87%E6%96%99-03.py

https://stackoverflow.com/questions/28133018/convert-pandas-series-to-datetime-in-a-dataframe

http://timestamp.online/

https://stackoverflow.com/questions/25640698/google-script-convert-date-to-epoch-time

"""
