#21-2-7
# iter_countent()
import requests

url='http://www.deepstone.com.tw'
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:
    print("網頁下載失敗: %s" % err)
#儲存網頁內容
fn = 'out21_11.txt'
with open(fn, 'wb') as file_Obj:    #以二進位儲存
    for diskStorage in htmlfile.iter_content(10240): #Reponse物件處理
        size = file_Obj.write(diskStorage)    #Reponse物件寫入
        print(size)    #列出每次寫入大小
    print("以 %s 儲存網頁HTML檔案成功" % fn)

"""
由於網頁內容比較小,所以每次寫入檔案大小設為10240bytes,程式中with之後所開啟的是以二進位可寫入"wb"方式開啟,這是為了怕網頁內有Unicode碼.
"""
    
