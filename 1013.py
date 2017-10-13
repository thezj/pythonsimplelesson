# 迭代器 可访问集合 字符串，元组，列表

list1 = [1, 2, 3]
it1 = iter(list1)  #创建迭代器对象
#输出迭代器的下一个元素，并把遍历的位置向前进一位
while False:
    try:
        print(next(it1))
    except StopIteration:
        exit()

# 使用了yield(产出) 的函数被称为生成器 generator（生成器）
# 生成器是一个返回迭代器的函数，只能用于迭代操作，简单理解就是一个迭代器
# 在运行生成器后，每次遇到yield时会暂停并保存当前所有的运行信息，立即返回yield的值，并在下一次运行next()时从当前位置继续运行。


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        # yield a
        print(a)
        a, b = b, a + b
        counter += 1


f1 = fibonacci(10)
list1 = []

while True:
    try:
        next(f1)
    except StopIteration:
        exit()

while True:
    try:
        list1.append(next(f1))
    except StopIteration:
        print(list1)
        exit()
