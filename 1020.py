for x in range(1, 11):
    # print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
    print(str(x).ljust(2), str(x * x).ljust(3), str(x * x * x).ljust(4))

print('{},{},{}'.format(1, 2, 3))
print('{2},{1},{0}'.format(1, 2, 3))
print('{firstname} {secondname}'.format(firstname='jim', secondname='zeng'))

import math
str1 = '斯蒂芬的身份{0:.3f}'.format(math.pi)
print(str1)

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]}; Google: {0[Google]}; Taobao: {0[Taobao]}'.format(
    table))

with open('./testfs.txt', 'w+', encoding='utf-8') as f:
    charnum = f.write('python是一个好的语言，\n是的，的s第一次确\n非常好\n')
    print('characternum:', charnum)
    # f.close() 处理文件对象
    '''
        使用with关键字是非常好的方式，
        在结束操作后
        它会帮组正确的关闭文件
    '''

with open('./testfs.txt', 'r', encoding='utf-8') as f:
    f.seek(9, 0)
    print(f.tell(), 'readline:', f.readlines())
    print(f.tell(), f.read())

with open('./testfs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

import pickle
data1 = {'a': 1, 'b': (2, 3)}
output = open('data.pk1','wb')
pickle.dump(data1,output)
output.close()

pk1file = open('data.pk1','rb')

data1return = pickle.load(pk1file)
pk1file.close()
print(data1return)

