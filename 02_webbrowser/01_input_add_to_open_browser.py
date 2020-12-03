#21-1-3
#地址查詢地圖的程式設計
import webbrowser
address = input('請輸入地址:')
webbrowser.open('http://www.google.com.tw/maps/place/' + address)
