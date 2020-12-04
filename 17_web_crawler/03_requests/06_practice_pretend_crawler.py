#21-2-6
#爬蟲程式偽裝成瀏覽器

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            safari/537.36',}

url = 'http://aaa.24ht.com.tw/'
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")
           
# "\" 表下一行跟這一行是相同敘述
           
"""
An EOL ( End of Line ) error indicates that the Python interpreter expected a 
particular character or set of characters to have occurred in a specific line 
of code, but that those characters were not found before the end of the line .
"""
