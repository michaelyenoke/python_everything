# Pandas 分割字串 : https://www.itread01.com/content/1550524862.html

# 在列表中切割字串

b=["5-9*13","6-10*14","7-11*15","8-12*16"]
for i in range(len(b)):
    b[i]=b[i].split("-",1)
----------
print(b)
[['5', '9*13'], ['6', '10*14'], ['7', '11*15'], ['8', '12*16']]
----------

# 資料框中切割字串

from pandas.core.frame import DataFrame
df = DataFrame({"a" : ["1","2","3","4"],
        "b" : ["5-9","6-10","7-11","8-12"]})
----------
print (df)
   a     b
0  1   5-9
1  2  6-10
2  3  7-11
3  4  8-12
----------
df['b'], df['c'] = df['b'].str.split('-', 1).str
----------
print (df)
   a  b   c
0  1  5   9
1  2  6  10
2  3  7  11
3  4  8  12
----------
