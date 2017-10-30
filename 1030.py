import os, sys


def get_py(path):
    filelist = os.listdir(path)
    for filename in filelist:
        pathtmp = os.path.join(path, filename)
        if os.path.isdir(pathtmp):
            get_py(pathtmp)
        elif filename[-3:].upper() == '.PY':
            print(filename)


# get_py('./') 查找‘./’目录下的.py(不限制大小写)后缀名文件

if True: print(11)

while True:
    try:
        x = int(input('please enter a number'))
        raise NameError('hithere')
    except ValueError as e:
        print('opps! that was no valid number, try again>>>>', e)
    except NameError as e:
        print('opps! there has a name error, try again>>>>', e)
    else:
        print('xxx')
