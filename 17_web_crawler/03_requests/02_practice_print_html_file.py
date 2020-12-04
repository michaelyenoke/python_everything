#21-2-2
#列印網頁原始碼
import requests
url='https://www.carrefour.com.tw/console/api/v1/stores?is24h=&page_size=all'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁成功")
else:
    print("取得網頁內容失敗")
print(htmlfile.text)



#21-2-2
#Response
import requests
url='http://decathlon.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁成功")
else: 
    print("取得網頁內容失敗")

    
    
#21-2-2
#擴充,取得網頁內容大小
import requests
url = 'https://www.decathlon.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁成功")
else:
    print("取得網頁內容失敗")
print("網頁內容大小=",len(htmlfile.text))
