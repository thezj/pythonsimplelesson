# 字典的每个键值对用冒号：分割，键值是唯一的，不可变的 字符串 数字 元组

dict1 = {'alice': 'string', 123.12: 'float', (1, 2): 'tuple'}
dict1[(1, 2)] = 'a tuple'
dict1[(1, 2, 3)] = 'other tuple'
del dict1[(1, 2, 3)]
print(dict1, dict1['alice'], dict1[123.12], dict1[(1, 2)])
print(len(dict1), str(dict1), type(dict1))
dict2 = dict1.copy()
print(dict2 is dict1, dict2.get((1, 2)), (1, 2) in dict2)
dict2list = dict2.items()
for dict2listi in dict2list:
    print(dict2listi)
dict3 = dict1.fromkeys(['alice', (1, 2)], 1)
dict3.setdefault((1, 2, 2), 'haha')
print(dict3)
print(dict1)
dict3.update(dict1)
print(dict3)
print(dict3.values())
dict3.pop((1, 2, 2))
print(dict3.values())
dict3.popitem()
print(dict3.values())
dict4 = {'sdf': {'1213': {'123': 2}}}
print(dict4['sdf']['1213']['123'])
print('====================')
a, b = 0, 1
while a < 100:
    print(a, end=',')
    a, b = b, a + b  # 复合赋值，变量a，b同时得到新值，不会出现a=b 后 b再等于新的a（b）加上b

