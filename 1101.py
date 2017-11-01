class myclass:
    #初始化构造函数，在生成对象时调用
    def __init__(self, age=10):
        self.initdata = age
        print('类初始化函数：', self, self.__class__)

    #析构函数，在对象释放时调用
    def __del__(self):
        print('我被释放了', self)

    #属性
    i = 123
    #类的私有属性,以两个下划线开头，不能在类外部直接访问,能在类内部使用(私有方法也是一样)
    __classage = '100'

    #方法,类的方法必须包含参数self，且为第一个参数，代表类的实例
    def f(self):
        return 'hello world' + self.__classage


class speaker:
    #多重继承时，出现同名方法默认调用的是在括号中最左边的类的方法
    def f(self):
        return '我覆盖了右边的类的方法'


class student(speaker, myclass):
    def __init__(self, name, age):
        myclass.__init__(self, age)
        self.name = name

    def speak(self):
        print('我叫{2}，我{0}岁了，我的i属性{1}'.format(self.initdata, self.i, self.name))

    #重写父类的方法
    def f(self):
        return '子类覆盖了父类的方法'


x = myclass()

print('myclass类的属性i：', x.i)
print('myclass类的初始化属性initdata：', x.initdata)
print('myclass类的方法f：', x.f())

s1 = student('jim', 33)
s1.speak()
print('student类的方法f：', s1.f())


class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector({0},{1})'.format(self.a, self.b)

    def __add__(self, other):
        print('被调用', self, other)
        return vector(self.a + other.a, self.b + other.b)


v1 = vector(2, 10)
v2 = vector(3, -5)
v3 = v1 + v2
print(v3)
