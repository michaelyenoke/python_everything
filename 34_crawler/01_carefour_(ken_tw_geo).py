# Web scarping for the store location info of Taiwan Carrefour.
# 1st step: Use Google Chrome and connect to TW Carrefour store info site > press "F12" to launch developer mode > click "XHR" to identify the API link
# https://docs.google.com/document/d/1d4fmOA7S1wOpbw72dwC8W71_I3SqyHc74Ka2dM_zZSk/edit
# 2nd step: Use postman app to test API link and identify the parameters for gathering data
# 3rd step: Use below PYTHON code to scarp information form the website.



import requests
import pandas as pd

# 建立一個區域的list

city = ['1','2', '3', '4', '5', '6', '7', '8'] 

# 1: 新北市
# 2: 台北市
# 3: 桃竹苗
# 4: 中彰投
# 5: 雲嘉南
# 6: 高屏
# 7: 宜花東
# 8: 金馬


box = []


#剛剛在開發者模式觀察到的get發出的資訊是那些
## python --python enumerate用法总结-- https://blog.csdn.net/churximi/article/details/51648388
## enumerate 可以比用range + list 寫的更加簡潔
## 最簡 print(list(enumerate(list1)))
for index, city in enumerate(city):
  # data 是要hit那個API endpoint的參數,從眾多參數中選取你所需要的 
  data = {                      
        'store_area_id':city,
        'is24h':'',
        'page_size':'all'
          }
  #print(data)
  res = requests.get(url = 'https://www.carrefour.com.tw/console/api/v1/stores', params=data)
  box.append(res.text)
  #print(box)
  
# 先定義 dataframe ---> store_table
store_table = pd.DataFrame(columns = ['store_name', 'store_address', 'store_type_name'])


def loop():
  for info in store_info:  # function 內未執行
    for k, v in info.items(): # k:key , v:value
        # http://tw.gitbook.net/python/dictionary_items.html : items()
      if k == 'name': # == 比較是否相等 ---> true or false
        name = v      # = 賦值
      elif k== 'store_type_name':  # 和if本身不互斥,像sql的case when;if...else...就是互斥
         store_type = v
      elif k == 'address':
         address = v
         new_row = {'store_name' : name, 'store_type_name' : store_type, 'store_address' : address}
         global store_table
         store_table = store_table.append(new_row, ignore_index= True)
         
         
#store_table = pd.DataFrame(columns = ['store_name', 'store_address', 'store_type_name'])

for i in range(len(box)):
  df_carrefour = pd.read_json(box[i])
  store_info =  df_carrefour.data.iloc[2]   # 限定只有store的資訊, items()會讀取我們要的範圍
  loop()

store_table.to_csv('家樂福門市.csv', encoding="UTF-8", index=False)





print(store_table)
  
  
