# 一个py文件，包含所有你定义的函数和变量，模块可以被别的程序引入，使用模块中的函数和变量

import sys, support1019
from support1019 import *

for i in sys.argv:
    print(i)

# print(sys.path)
support1019.hi('hello')
hi('hello1')
print(supportvar1)

print(dir(
    support1019))  # dir可以找到模块内定义的所有名称。以一个字符串列表形式返回，包含内置的‘__name__,__file__’等
print(dir())