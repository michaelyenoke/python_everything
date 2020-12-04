#21-2-3
#搜尋網頁特定內容

import requests
import re
url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JYcG9MVlJYR2dKVVZ5Z0FQAQ/sections/CAQiXkNCQVNRQW9JTDIwdk1ESnFhblFTQlhwb0xWUlhHZ0pVVnlJT0NBUWFDZ29JTDIwdk1ESjJlRzRxR1FvWENoTk5UMVpKUlZOZlUwVkRWRWxQVGw5T1FVMUZJQUVvQUEqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURKcWFuUVNCWHBvTFZSWEdnSlVWeWdBUAFQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("請輸入欲搜尋的字串:")  #pattern存放欲搜尋的字串  
    #使用方法1
    if pattern in htmlfile.text:
         print("搜尋 %s 成功" % pattern)  # %d , %s , % 的用法參考 p.4-4
    else:
         print("搜尋 %s 失敗" % pattern)
    #使用方法2
    # re 模塊 http://blog.fantasy.codes/python/2013/07/02/py-re-module/
    name = re.findall(pattern, htmlfile.text) #方法2
    if name != None:
        print("%s 出現 %d 次" % (pattern, len(name)))
    else:
        print("%s 出現 0 次" % pattern)

else:
    
    print("網頁下載失敗")
