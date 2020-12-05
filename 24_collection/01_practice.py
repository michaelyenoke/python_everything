# https://docs.python.org/2/library/collections.html#module-collections
# collections : https://www.zlovezl.cn/articles/collections-in-python/

"""
我们都知道，Python拥有一些内置的数据类型，比如str, int, list, tuple, dict等， collections模块在这些内置数据类型的基础上，提供了几个额外的数据类型：

namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
deque: 双端队列，可以快速的从另外一侧追加和推出对象
Counter: 计数器，主要用来计数
OrderedDict: 有序字典
defaultdict: 带有默认值的字典
"""

# namedtuple()

from collections import namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print website 

# deque()

import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)
    
# conter()

from collections import Counter

s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()

c = Counter(s)
# 获取出现频率最高的5个字符
print c.most_common(5)

# OrderedDict

from collections import OrderedDict

items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print 'Regular Dict:'
for k, v in regular_dict.items():
    print k, v

print 'Ordered Dict:'
for k, v in ordered_dict.items():
    print k, v
    
# defaultdict

from collections import defaultdict

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]

result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)

print result
    

    
