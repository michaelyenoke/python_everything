#21-2-4
#下載網頁失敗的異常處理
#Reponse 物件有 raise_for_status(),可以針對網址正確但是後續檔案名稱錯誤的狀況產生異常處理

import requests

url = 'http://www.yahoo.com/file_not_exit' # 不存在的內容
htmlfile = requests.get(url)
try:                              # try參考 p15-3 
    htmlfile.raise_for_status()   #異常處理
    print("下載成功")
except Exception as err:          # except參考 p15-11 # Exception - 常見的異常物件 p15-8 - 一般錯誤皆可使用
    print("網頁下載失敗: %s" % err)
    
    
""""
try:
    指令           #預先設想可能引發錯誤異常的指令
except 異常物件    
    異常處理程序    #通常是指出異常原因,方便修正
"""    
