import random
age = int(input('请输入你家狗狗的年龄：'))
if age < 0:
    print('invalid')
elif age == 1:
    print('相当于14岁的人。')
elif age == 2:
    print('相当于22岁的人')
elif age > 2:
    human = 22 + (age - 2) * 5
    print('对应的人类年龄:', human)
number, guess = 1, 2
while guess != number:
    number = random.randrange(1, 4)
    guess = int(input('请输入你猜的数字：'))
    if guess == number:
        print('你猜对了')
    elif guess < number:
        print('小了')
        guess1 = int(input('second chance:'))
        if guess1 == number:
            print('对了')
            guess = number
    else:
        print('大了')