# Python 類別的定義與使用

# 定義類別, 與類別屬性 (封裝在類別中的變數和函式)
# 定義一個類別 IO, 有兩個屬性 supportedSrcs 和 read
class IO:
    suppportedSrcs=["console","file"]
    def read(src):
        print("Read from", src)
        
        
# 使用類別 : 類別名稱 + 屬性名稱
print(IO.suppportedSrcs)

IO.read("file")

class IO:
    suppportedSrcs=["console","file"]
    def read(src):
        if src not in IO.suppportedSrcs:
            print("Not Supported")
        else:
            print("Read from", src)
            

IO.read("file")

IO.read("internet")

# Python 基礎 - class : 類

"""
觀念:

1. 一開始其實與寫 fuction 是一樣的,先寫出 class 的名稱(通常大寫), 然後寫出 def 的內容出來, 像是 add(x,y) 
2. 之後, 再為這個 class 增加一些屬性進去, 像是 name, price 等
3. 加入了自定義的屬性之後, 在 def 內就要加入 self 作為第一個參數, 代表引用自身 class 的屬性, 如 self.name
"""
def method(self,value):
    self.attribute = value
    
class Calculator:   
    name = 'Good calculator'
    price = 18
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        Print(x/y)        
        
        
calcul = Calculator() # 個體 = 類型   ---> 方便調用類型
calcul.name
calcul.price

# Python 類別的實體屬性與實體方法:Python 專案開發入門的十堂課

"""
1. ___init__()方法是Python類別中的一個特殊方法,是在物件建立的過程中執行的方法,也就是
   俗稱的建構子
   
2. __str__() 物件中預設的字串表達形式,在呼叫內建函數 print() 的時候, 就會直接印出 
  __str__() 所回傳的字串,一般來說,類別會有預設的 __str__()方法,也就是預設的物件表達形
  式字串,如果需要自己自定的物件表達字串,就需要重新定義__str__()方法
"""

class Demo2:
    def __init__(self,i):
        self.i = i
    def hello(self):
        print("Hello", self.i)

d = Demo2(9527)
d.hello()
   
class Demo3:
    pass

d = Demo3()
print(d)

class Demo4:
    def __init__(self,i):
        self.i = i
    def __str__(self):
        return str(self.i)

d = Demo4(9528)
print(d)
