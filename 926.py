if True:
    print('True')
else:
    print('False')
    print('answer')

total = 3 + 3 + 4\
        +2
array = ['itemone', 'itemtwo', 'itemthree', 'itemfour\nsss']

string = r'sdfsdfsdf\nsdfsdf'
string = '''sss

sdfsdf'''
print(total, 2, array, string, end='\n')
# inputstring = input()
# print('你输入了', inputstring)

import sys

print('=================Python import mode==================')
print('命令行参数为：', sys.argv)

for i in sys.argv:
    print(i)

print('\n python路径为', sys.path)

from sys import argv as sss, path

print(sss)

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

import types

typestring = [type(type(counter)), type(miles), type(name)]

print(typestring)

num1 = num2 = num3 = 3

num1, num2, num3, num4 = 2, 3, 4, 5
print(num1, num2, num3, num4)
print(type(True))
print(type(0 + 1j))


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(isinstance(B(), A))
print(type(A()) == A)
print(type(B()) == A)

print(True + 1)
# del num1
print(num1)
print(7 % 3, 3**3, 5 // 3)  #// 取整除法是向下取整数

str2 = 'jim'

print(str2)
print(str2[0:-1])
print(str2[1])
print(str2[0:])
print(str2 * 3)
print(str2 + 'TEST')

list1 = [1, 1.0, 3 + 2j, 'sss']
list2 = [222, 'jim']

print(list1)
print(list1[0])
print(list1[0:])
print(list1[0:-1])
print(list1 * 2)
list2[1] = 'lilian'
print(list1 + list2)

tuple1 = ('abcd', 123, 1.0, 2 + 2j)
tuple2 = ('jim', )  #('ssss') this is a string
print(type(('jim')), end='=========\n')
print(type(tuple1))
print(tuple1[0])
print(tuple1[0:2])
print(tuple1[2:])
print(tuple1 * 2)
print(tuple1 + tuple2)

student = {'tom', 'jim', 'mary', 'tom', 'jack', 'rose'}

print(student)  #输出集合，重复元素自动去掉

# 成员测试
if 'jim' in student:
    print('has rose')
else:
    print('haven t rose')

seta = set('12345')
setb = set('123789')

print(seta)
print(seta - setb)
print(setb - seta)
print(setb | seta)
print(setb & seta)
print(setb ^ seta)

dict1 = {}
dict1['one'] = 'jim'
dict1[2] = 'lilian'

print(dict1)
print(dict1['one'])
print(dict1.keys())
print(dict1.values())

dict2 = dict([('a', 1), ('b', 2)])
dict3 = dict(a=3, b=4)

print(dict2)
print(type(dict3))
print(type(str(dict3)))

#
#   number : 1 , 2.0 , 1+2j
#   sequence : string list tuple
#   set: 无序不重复序列，基本功能是进行成员关系测试、删除重复元素，可使用｛｝或者set（）构造函数创建集合。
#   dictionary:字典是无序对象集合，通过键来取得值，无序的key：value对集合，key为不可变类型，key必须是唯一
#

dictx = {'a': 1, 'b': 2}
representx = str(dictx)
dictxx = eval(representx)
print(type(dictxx), dictxx)
