# 函数是组织好的可复用实现单一或相关功能的代码段
# def关键字开头，后接函数名称和圆括号，传入参数和自变量放在括号中，然后是冒号
# return 语句 结束函数，选择性的返回一个值给调用方，不带return返回none

a = 'hi'
dict1 = {a: 1}


def hello(a, b=10):
    if type(a) == dict:
        a['hi'] = 2
    else:
        a = 'hello'
    print(a, b)
    return 'some expression'


hello(a)
print(a)

hello(dict1)
print(dict1)

hello('呀', '好')
hello(b='呀', a='好')


def variableparams(arg1, *params):
    '函数文档字符串'
    print(params)


variableparams(10, 100, 11)
'''
使用lambda,lambda有自己的命名空间，不能访问自己参数列表之外，或全局命名空间里的参数
'''

sum = lambda arg1, argx=10, *arg2: arg1 + arg2[0]

print(sum(1, 2, 3))

print(hello(5))


def outer():
    outer_a = 1

    def inner():
        nonlocal outer_a
        outer_a += 2
        # outer_a = outer_a + 2 # 等号左边的outer_a是局部变量 没有定义不能修改
        print(outer_a)

    return inner


# print(outer_a) outer_a is not defined

innerinstance = outer()
innerinstance()
innerinstance()
innerinstance()

if True:
    msg = 'im form python'

print(msg)

total = 0


def sum(a1, a2):
    global total  # 要修改外部全局变量需要加 global关键字
    total = a1 + a2
    print(total)


sum(2, 3)
print(total)
