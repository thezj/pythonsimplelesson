# python 中循环语句有 for while

n, sum, counter = 100, 0, 1
while counter <= n:
    sum += counter
    counter += 1
print('1 到 %d 之和为：%d' % (n, sum))

# while 1:
#     num = input('请输入：')
#     print(num)

count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
print(count, " 大于或等于 5")

string1 = '12345'

for character in string1:
    if character == '2':
        print('找到了')
        break
    print(character)
else:
    print('没有循环数据')


for i in range(3):
    print(i)

