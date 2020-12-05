# glob — Unix style pathname pattern expansion : https://docs.python.org/3/library/glob.html
# python標準庫之glob介紹 : https://www.twblogs.net/a/5d668e41bd9eee541c3356bc
# Python 中使用 UNIX 規則匹配檔案的模組 glob : https://clay-atlas.com/blog/2019/10/26/python-chinese-tutorial-packages-glob/ 

"""
glob 文件名模式匹配，不用遍歷整個目錄判斷每個文件是不是符合。

用它可以查找符合特定規則的文件路徑名。跟使用windows下的文件搜索差不多。
查找文件只用到三個匹配符：””, “?”, “[]”。””匹配0個或多個字符；”?”匹配單個字符；”[]”匹配指定範圍內的字符，如：[0-9]匹配數字。
"""

import glob
for name in glob.glob('dir/*'):
    print (name)
