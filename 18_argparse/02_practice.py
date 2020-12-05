# Python Tutorial - Argparse : https://www.youtube.com/watch?v=cdblJqEUDNo

# This program calculates the volume of cylinder given RADIUS and HEIGHT
# Cylinder Volume = (pi)*(radius ** 2) * (height)

import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('-r', '--radius', type=int, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, help='Height of Cylinder')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol

if __name__ == '__main__':
    print cylinder_volume(args.radius, args.height)


######  section ######

#!/usr/bin/env python3  
import argparse  
  
parser = argparse.ArgumentParser()  
# nargs='+' takes 1 or more arguments, nargs='*' takes zero or more.  
parser.add_argument('-l','--list', nargs='+', help=' Set flag', required=True)  
args = parser.parse_args()  
print("Given list: {}".format(args.list))  

###### section #####

cmd : py arg_learning2.py -l/--list


###### section #####

#!/usr/bin/python3
import argparse
 
parser = argparse.ArgumentParser(description="這是說明敘述")
 
parser.add_argument('-c', help='testing c')
parser.add_argument('-d', help='testing d')
parser.add_argument('-f', help='testing f')
 
args = parser.parse_args()
 
if args.c:
    print('flag c :', args.c)
if args.d:
    print('flag d :', args.d)
if args.f:
    print('flag f :', args.f)
    
    
###### section ######

cmd :py arg_learning.py -c C    


###### section ######

"""
argparse
argparse 是 Python 内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，argparse 将会从 sys.argv 中解析出这些参数，并自动生成帮助和使用信息。

https://wiki.jikexueyuan.com/project/explore-python/Standard-Modules/argparse.html

argparse 使用
简单示例
我们先来看一个简单示例。主要有三个步骤：

创建 ArgumentParser() 对象
调用 add_argument() 方法添加参数
使用 parse_args() 解析添加的参数
"""


###### section ######


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integer', type=int, help='display an integer')
args = parser.parse_args()

print(args.integer)

###### section ######
"""
$ python argparse_usage.py
usage: argparse_usage.py [-h] integer
argparse_usage.py: error: too few arguments

$ python argparse_usage.py abcd
usage: argparse_usage.py [-h] integer
argparse_usage.py: error: argument integer: invalid int value: 'abcd'

$ python argparse_usage.py -h
usage: argparse_usage.py [-h] integer

positional arguments:
  integer     display an integer

optional arguments:
  -h, --help  show this help message and exit

$ python argparse_usage.py 10
10


定位参数
上面的示例，其实就展示了定位参数的使用，我们再来看一个例子 - 计算一个数的平方：

"""

###### section ######

# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)

###### section ######

"""
$ python argparse_usage.py 9
81

可选参数
现在看下可选参数的用法，所谓可选参数，也就是命令行参数是可选的，废话少说，看下面例子：
"""

# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--square", help="display a square of a given number", type=int)
parser.add_argument("--cubic", help="display a cubic of a given number", type=int)

args = parser.parse_args()

if args.square:
    print(args.square**2)

if args.cubic:
    print(args.cubic**3)
    
    
"""
$ python argparse_usage.py --h
usage: argparse_usage.py [-h] [--square SQUARE] [--cubic CUBIC]

optional arguments:
  -h, --help       show this help message and exit
  --square SQUARE  display a square of a given number
  --cubic CUBIC    display a cubic of a given number

$ python argparse_usage.py --square 8
64

$ python argparse_usage.py --cubic 8
512

$ python argparse_usage.py 8
usage: argparse_usage.py [-h] [--square SQUARE] [--cubic CUBIC]
argparse_usage.py: error: unrecognized arguments: 8

$ python argparse_usage.py  # 没有输出
"""

##### section ######

"""
混合使用
定位参数和选项参数可以混合使用，看下面一个例子，给一个整数序列，输出它们的和或最大值（默认）：
"""

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


"""
$ python argparse_usage.py
usage: argparse_usage.py [-h] [--sum] N [N ...]
argparse_usage.py: error: too few arguments
$ python argparse_usage.py 1 2 3 4
4
$ python argparse_usage.py 1 2 3 4 --sum
10
"""

"""
add_argument() 方法
add_argument() 方法定义如何解析命令行参数：
"""

"""
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
"""

"""
每个参数解释如下:

name or flags - 选项字符串的名字或者列表，例如 foo 或者 -f, --foo。
action - 命令行遇到参数时的动作，默认值是 store。
store_const，表示赋值为const；
append，将遇到的值存储成列表，也就是如果参数重复则会保存多个值;
append_const，将参数规范中定义的一个值保存到一个列表；
count，存储遇到的次数；此外，也可以继承 argparse.Action 自定义参数解析；
nargs - 应该读取的命令行参数个数，可以是具体的数字，或者是?号，当不指
        定值时对于  
        Positional argument 使用 default，对于 Optional argument         使用 const；或者
        是 * 号，表示 0 或多个参数；或者是 + 号表示 1 或多个参数。
const - action 和 nargs 所需要的常量值。
default - 不指定参数时的默认值。
type - 命令行参数应该被转换成的类型。
choices - 参数可允许的值的一个容器。
required - 可选参数是否可以省略 (仅针对可选参数)。
help - 参数的帮助信息，当指定为 argparse.SUPPRESS 时表示不显示该参数的帮助信息.
metavar - 在 usage 说明中的参数名称，对于必选参数默认就是参数名称，对于可选参数默认是
          全大写的参数名称.
dest - 解析后的参数名称，默认情况下，对于可选参数选取最长的名称，中划线转换为下划线.
"""

"""
https://docs.python.org/3/howto/argparse.html
"""

"""
How to: Add a verbose argument to the CLI
RELATED
Add a non-optional argument to the CLI

Add a help message to an argument for the CLI

Add an optional argument (flag) to the CLI

Add an epilogue to the CLI

Add a description to the CLI

Add a custom attribute name destination to the CLI
"""


##### section ######

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="modify output verbosity", action = "store_true")
parser.print_help()
