#ch22_4.py
from selenium import webdriver

driverPath = 'C:/Users/MichaelCHEN/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = 'http://www.google.com'
browser.get(url)
