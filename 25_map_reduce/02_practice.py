"""



Python 里为什么函数可以返回一个函数内部定义的函数？ https://www.zhihu.com/question/25950466

python中reduce()函数
reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，
一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个
元素反复调用函数f，并返回最终结果值。

python中map()函数 :https://www.imooc.com/code/6049
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
例如，对于list [1, 2, 3, 4, 5, 6, 7, 8, 9]
如果希望把list的每个元素都作平方，就可以用map()函数：

"""

def caller_func(f):
    return f(1, 2)
    
    
def f(x):
    return x*x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def format_name(s):
    return s[0].upper() + s[1:].lower()
print map(format_name, ['adam', 'LISA', 'barT'])
    
