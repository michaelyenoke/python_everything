from bs4 import BeautifulSoup
import requests, bs4

htmlFile = requests.get('http://www.yahoo.com.tw')
#objSoup = bs4.BeautifulSoup(htmlFile.text,'html5lib')
objSoup = bs4.BeautifulSoup(htmlFile.text,'lxml')
# html.parser - 老舊方法,相容性較不好; lxml - 速度快,相容性佳; html5lib - 速度慢,解析力強
print("列印BeautifulSoup物件資料型態", type(objSoup))
