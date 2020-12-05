#ch22_5.py # 找到元素
from selenium import webdriver

driverPath = 'C:/Users/MichaelCHEN/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)   # 網頁下載至瀏覽器
tag = browser.find_element_by_id('content')
print(tag.tag_name)


#ch22_5.py # 列出找不到元素,造成程式結束的實例
from selenium import webdriver

driverPath = 'C:/Users/MichaelCHEN/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)   # 網頁下載至瀏覽器
tag = browser.find_element_by_id('main')
print(tag.tag_name)
