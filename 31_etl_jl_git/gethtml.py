import os
import requests
#import jsonlines
#import simplejson
#import json

#print(os.getcwd()) 
#取得當前資料夾位置

#print(os.path.abpath('.'))
#取得絕對位置


html = requests.get("https://api.kcg.gov.tw/api/service/get/b003ef1f-6179-4070-b154-45b818d5e8fa")

#html = requests.get("https://data.ntpc.gov.tw/od/data/api/54172EE2-975D-44C6-9465-9719E5EF5264?$format=json").json()
#加上.json()後從原來的「"」變成「'」反而不是json格式,變成python格式 


print(html.text)

#list1 = eval(html.text)   # eval 取出json檔案中的list值
#for dict in list1:        # 透過for迴圈依序將 dict 取出
#    listvalues = list(dict.values()) # 將 dict 的值排成 list
#    print(listvalues)
                    
                    
#j = simplejson.loads(str) #simplejson 可以有效使用 loads, dumps等函數                    
                    
                    
