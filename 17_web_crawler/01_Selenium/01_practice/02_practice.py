#ch22_3.py
from selenium import webdriver

driverPath = 'C:/Users/MichaelCHEN/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe'
browser = webdriver.Chrome(driverPath)
print(type(browser))

"""
Download and unzip chromedriver and put 'chromedriver.exe' in C:\Python27\Scripts and then you need not to provide the path of driver, just

driver= webdriver.Chrome()
"""
