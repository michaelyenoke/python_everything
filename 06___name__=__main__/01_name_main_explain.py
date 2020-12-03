
#!/usr/bin/env python
# coding: utf-8

# ### Python - if __name__ == '__main__' 涵義
# http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html
"""
首先，如果你永遠都只執行一個 Python 檔，而不引用別的 Python 檔案的話，那你完全不需要了解這是什麼。例如你寫了一個很棒的函式 cool.py：
# In[1]:
"""

# cool.py

def cool_func():
    print('cool_func(): Super Cool!')

    
print('Call it locally')
cool_func()

"""
這完全沒有問題。問題會出在當你想要在別的檔案中使用你在 cool.py 中定義的函式時，例如你在相同目錄下有一個 other.py：
# In[ ]:
"""

# other.py

from cool import cool_func

print('Call it remotely')
cool_func()

"""
看到問題了嗎？cool.py 中的主程式在被引用的時候也被執行了，原因在於：

1.當 Python 檔案（模組、module）被引用的時候，檔案內的每一行都會被 Python 直譯器讀取並執行（所以 cool.py內的程式碼會被執行）

2.Python 直譯器執行程式碼時，有一些內建、隱含的變數，__name__就是其中之一，其意義是「模組名稱」。如果該檔案是被引用，其值會是模組名稱；但若該檔案是(透過命令列)直接執行，其值會是 __main__；。所以如果我們在 cool.py 內加上一行顯示以上訊息：
# In[3]:
"""

# cool.py

def cool_func():
    print('cool_func(): Super Cool!')

print('__name__:', __name__)
print('Call it locally')
cool_func()

"""
再分別執行 cool.py 與 other.py，結果會是：
# In[ ]:
"""

"""
# >> python cool.py

__name__: __main__     # 這裡的 __name__ 印出來的是 main
Call it locally
cool_func(): Super Cool!

# >> python other.py

__name__: cool        # 這裡的 __name__ 印出來的是 cool , 原來檔案的檔案名
Call it locally
cool_func(): Super Cool!
Call it remotely
cool_func(): Super Cool!
"""


"""
你就可以看到 __name__ 的值在檔案被直接執行時與被引用時是不同的。所以回到上面的問題：要怎麼讓檔案在被引用時，不該執行的程式碼不被執行？當然就是靠 __name__ == '__main__'做判斷！
# In[4]:
"""

# cool.py

def cool_func():
    print('cool_func(): Super Cool!')

if __name__ == '__main__':    # 所以在引用其他的程式文檔,只有確定出於原文檔
    print('Call it locally')
    cool_func()

"""
執行結果是:
# In[ ]:
"""
"""
#>> python cool.py

Call it locally
cool_func(): Super Cool!

>> python other.py

Call it remotely
cool_func(): Super Cool!

問題就完美解決了！最後一點要說明的是，之所以常看見這樣的寫法，是因為該程式可能有「單獨執行」（例如執行一些本身的單元測試）與「被引用」兩種情況，因此用上述判斷就可以將這兩種情況區分出來。希望這篇文章有解答到你的疑問。
# ### Python混合用法模式：name__和 _main
# 
# 原文網址：https://kknews.cc/tech/ae4v5yv.html

# In[ ]:
"""



