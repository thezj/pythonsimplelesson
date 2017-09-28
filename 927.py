#这是单行注释
'''
多行
注释
'''
print('hello world')

a, b = 10, 20
c = a + b
print(c)
c //= a
print(c)
print(not (True and b))

#成员运算符
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 8]
print(a in list1)
print(a not in list1)

#身份运算符
# is用于判断两个变量引用对象是否是同一个内存
# == 用于判断引用变量的值是否相等
a, b = 10, 10
print(a is b)
print(a is not b)

a = [1, 2, 3]
b = a
print(a is b, a == b)
b = a[0:]  # b和a 已经是不同内存地址 但是 他们存储的值是相等的
print(a is b, a == b)
print(1 and False and 34)

a = 0b00111100
b = 0b00001101
print(bin(a & b))
print(bin(a | b))
print(bin(a ^ b))
print(bin(~a))
print(bin(a << 2))
print(bin(a >> 2))
print(a >> 2)

# 0x 16进制 0o 8进制 0b 2进制
print(0x10)
print(0b10)
print(0o10)

# 数据类型转换
print(complex(3, 5).imag)

import math
import random

print(17**3)
print(round(2.123456789, 2))
shufflea = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(shufflea)
print(shufflea)
print(math.floor(random.uniform(1, 9)))
