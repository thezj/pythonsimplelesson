str1 = 'hello123'
str2 = 'jim22 222'

print(str1, str1[0])
print(str2, str2[3:])
print(str2[0:3])
print(str2[:3])

print('123\\\'\"\a\b\000\n\v\t\r\f\o12456')
print(r'123\\\'\"\a\b\000\n\v\t\r\f\o12456')

#字符串格式化，%s 字符串 %d整数 %f浮点数

print('i am %s im %s an im %d years old' % ('jim', 'haha', 10))

print('''
    123
    123\t456\n123
    <html>
    <hr>
    </html>
''')

print(str.capitalize('abcd'))
print(str2.center(12, '*'))
print(str2.count('22', 4, len(str2)), len(str2))
print(str2.endswith('22', 0, 3))
print(str2.find('22'))  #返回索引值，否则返回-1
print(str2.index('22'))
print(str2.isalnum())  #字符串只包含数字、字母。至少一个字符character
print(str2.isalpha())  #字符串只包含字母。至少一个字符character
print(str2.isdigit())  #字符串只包含数字。至少一个字符character
print('abcd I'.islower())  #全部字母小写，至少包含一个小写字符
print(str2.join(('s', 'b')))
print(len(str2))
print('   123sd   '.lstrip().rstrip())
print(max('123 ABcz'))
print(min('123ABcz'))
print('111123ABcz'.replace('1', '8', 2))
print('1&2&s&xcc&234'.split('&'))
print('''
sdfs
sdf
sdf
sdfsss
'''.splitlines())

print('123'.startswith('2'))
print(' sdf  '.strip())
print(' sdf  '.swapcase())
print(' sdf  '.title())
intab = '12345'
outtab = 'abcde'
trantab = str.maketrans(intab,outtab)
preparestr = '78971hj45'
print(preparestr.translate(trantab))
print('ad'.upper())
print('ad'.zfill(5))
print('123010'.isdecimal())