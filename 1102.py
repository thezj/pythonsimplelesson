import os
import shutil
# print(os.getcwd())
# os.chdir('./today')
# os.system('mkdir today')
# print(dir(os))
shutil.copyfile('./testfs.txt', './testfstemp.txt')
# shutil.move('./xxxdir', './today/today')

import glob
print(glob.glob('*1.py'))

import sys
print(sys.argv)

import re
print(
    re.findall(r'(\bf[a-z]*)\s+\1\b',
               'fuck xffxxx fxxk feer   feer adf ,sdfkjsdlfjlfjsdjf'))
print(re.sub(r'\bf[a-z]*', '', 'fuck xffxxx fxxk feer adf ,sdfkjsdlfjlfjsdjf'))
print(
    re.sub(r'(\bf[a-z]*)\s+\1\b', r'\1',
           'fuck xffxxx fxxk 1 feer   feer 1 adf ,sdfkjsdlfjlfjsdjf'))

import random
print(random.choice(range(3)))
print(random.sample(range(3), 3))
print(random.random())
print(random.randrange(3))
'''
import urllib
from urllib.request import urlopen
for line in urlopen('http://www.newmotor.com.cn'):
    line = line.decode('GBK')
    imgsrc = re.findall(
        r'http://[^\'\"]*.jpg|http://[^\'\"]*.png|http://[^\'\"]*.gif', line)
    if len(imgsrc) != 0:
        print(imgsrc[0])
        urllib.request.urlretrieve(imgsrc[0], './today/' + str(random.random())[2:]+imgsrc[0][-4:])
'''

from datetime import date

now = date.today()
print(now.strftime('%y,%m,%d,'))
birthday = date(1989, 10, 10)
age = now - birthday
print(age)