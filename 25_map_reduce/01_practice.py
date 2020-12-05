"""
python中map()函数
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

例如，对于list [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def f(x):
    return x*x
print(map(f,[1,2,3,4,5]))

# 利用add(x,y,f)函数，计算：

import math
def add(x, y, f):
    return f(x) + f(y)
print add(25, 9, math.sqrt)

def add(x,y,f):
    return f(x)+f(y)
    

add(-9,-9,abs)

abs(-10)

f = abs

f(-20)

请利用切片，取出：

1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。

要取出3, 6, 9可以用::3的操作，但是要确定起始索引。

参考代码:
    
L = range(1, 101)
print L[:10]
print L[2::3]
print L[4:50:5]

def f1(x):
    return x*2
    
f1(4)


def new_fn(f):
    def fn(x):
        print('call'+ f._name_+'()')
        return f(x)
    return fn
    
g1 = new_fn(f1)
g1(4)

g1 = new_fn(f1)
g1(4)

def foo():
    print("foo")

def bar(func):
    func()

bar(foo)




