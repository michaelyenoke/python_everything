import pygsheets
gc = pygsheets.authorize(service_file='/Users/max/Desktop/Google python.json')

def f1(h):
    return h*2
def new_fn(k):
    def fn(p):
        print k.__name__
        print 'call' + k.__name__ + '()'
        print k(p)
        return k(p)
    print fn 
    return fn
    
g1 = new_fn(f1)
print g1(5)

def f1(x):
    return x*2
def new_fn(k):
    def fn(x):
        print k.__name__
        print 'call' + k.__name__ + '()'
        return k(x)
    return fn
    
f1 = new_fn(f1)
print f1(5)

print f(5)

def cont(x):
    print 'call f1()'
    return x*2

k = cont(4)

print k

print cont(2)

def f(x):
    return x*x
    
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            return j*j
        
            #def g():
            #    return j*j
            #return g
        r = f(i)
        fs.append(r)
    return  fs
    
print count()

f5, f6, f7 = count()
print f5(), f6(), f7()

f5()

f2()

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

f4 = count()

f4()

def g():
    print 'g()....'
    
def f():
    print 'f()....'
    return g

f()

g()


def f():
    print 'f()...'
    def g():
        print 'g()...'
    return g()

f()

g()


def is_odd(x):
    return x%2 == 1
    
    
filter(is_odd,[1,4,6,7,9,12,17])

def f(x):
    return x*x
print map(f,[1,2,3,4,5,6,7,8,9])

def add(x,y,f):
    return f(x)+f(y)
    
add(-5,9,abs)

def f1(x):
    return x*3
    
f1(5)  

def new_fn(f):
    def fn(x):
        print 'call'+f._name_ +'()'
        return f(x)
    return fn
    
g1 = new_fn(f1)
print g1(5)

f1 = new_fn(f1)
print f1(5)

def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()

f = calc_prod([ 2, 4, 6])
print f()

f = calc_prod([ 2, 4, 6])
print f()

y = f()

y()
