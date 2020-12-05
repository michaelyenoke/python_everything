# ch22_6.py # 找不到符合條件的元素時,執行例外處理 # 解決 ch22_5.py 報錯問題

from selenium import webdriver

driverPath = 'C:/Users/MichaelCHEN/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)   # 網頁下載至瀏覽器

try:
    tag = browser.find_element_by_id('main')
    print(tag.tag_name)
except:
    print("沒有找到相符的元素")
