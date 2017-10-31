class MyError(Exception):
    def __init__(this, value):
        print(type(this))
        this.value = value

    def __str__(this):
        return repr(this.value + 2)


try:
    raise MyError(3)
except MyError as e:
    print('my exception occurred, value:', e)
finally:
    print(222)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result:', result)
    finally:
        print('executing finally clause')


divide(2, 2)
divide(2, 0)
# divide(2, '2')


# 关键字with 可以保证 诸如文件之类的对象 在使用完之后一定会正确的执行他的清理方法，如：文件会被关闭
with open('./testfs.txt',encoding='UTF-8') as f:
    for line in f:
        print(line)