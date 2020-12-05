import requests
import pandas as pd

res = requests.get('https://www.carrefour.com.tw/console/api/v1/stores?store_area_id=1&is24h=&page_size=all')
print(res.text)
 
df_carrefour = pd.read_json(res.text)  #因為是json檔
 
print(df_carrefour)
 
df_carrefour.to_csv('家樂福門市.csv', encoding="UTF-8", index=False)
