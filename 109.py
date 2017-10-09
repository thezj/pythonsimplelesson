# python 的元组和列表类似，不同的是 元组的元素不能修改
list1 = [1, 2, 3]
tuple1 = (1, )
print(type(tuple1))
tuple1 = (1, 2, 3, '22')
tuple2 = (4, )
list1[2] = 4
# tuple1[2] = 4 tuple object does not support item assignment
print(list1[2], tuple1[1:-1])
tuple3 = tuple1 + tuple2
print(tuple3)
del tuple3
# print(tuple3) name 'tuple3' is not defined
#  max(tuple1) not supported between instances of 'str' and 'int'
print(len(tuple2), tuple1 + (4, ), tuple2 * 1, 3 in tuple1, tuple([2, 3]))
for x in tuple1:
    print(x)
