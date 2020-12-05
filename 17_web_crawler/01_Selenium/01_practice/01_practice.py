#  Selenium 透過模仿整個瀏覽器去抓取資料

# Python-- Selenium用法 : https://www.itread01.com/content/1541166610.html#8%EF%BC%9A%E8%8E%B7%E5%8F%96%E5%85%83%E7%B4%A0%E4%BF%A1%E6%81%AF

from selenium import webdriver

driverPath = 'C:/Users/MichaelCHEN/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)   # 網頁下載至瀏覽器


#tag1 = browser.find_element_by_tag_name('title')
#print("標籤名稱 = %s, 內容是 = %s" % (tag1.tag_name,tag1.text))


#tag2 = browser.find_element_by_id('author')
#print("\n標籤名稱 = %s, 內容是 = %s" % (tag2.tag_name,tag2.text))

tag3 = browser.find_element_by_id('content')
for i in range(len(tag3)):
    print("標籤名稱 = %s, 內容是 = %s" % (tag3[i].tag_name,tag3[i].text))
