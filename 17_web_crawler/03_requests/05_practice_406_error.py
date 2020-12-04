#21-2-5
#網頁伺服器阻擋造成讀取錯誤

import requests

url = 'http://aaa.24ht.com.tw/'
htmlfile = requests.get(url)
htmlfile.raise_for_status()

#HTTPError: 406 Client Error: Not Acceptable for url: http://aaa.24ht.com.tw/
#406錯誤就是網頁伺服器阻擋,用raise_for_status()可以快速中斷協助我們偵測錯誤
