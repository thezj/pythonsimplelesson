from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
print(queue)


def increaseit(num):
    return num + 2


samesequence = [1, 2, 3]
anothersequence = [increaseit(x) for x in samesequence if x < 2]
print(anothersequence)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print([[row[i] for row in matrix] for i in range(4)])

# print([[row[i] for row in matrix] for i in range(4)])

t = 1, 2, 3
print(t)

set1 = {1, 1, 1, 2}
set2 = {2, 3, 4}

print(set1)
print(set2 - set1, set1 | set2, set1 & set2, set1 ^ set2)

print(dict([(1, 2), (3, 4)]))
print({x for x in range(3)}, type({x for x in range(3)}))
print({x: 2 for x in range(3)}, type({x: 2 for x in range(3)}))

for k, v in {x: 2 for x in range(2)}.items():
    print(k, ':', v)

for i, v in enumerate([1, 2, 3]):
    print(i, v)

questions = ['name', 'quest']
answers = ['jim', 'frail']

for q, a in zip(questions, answers):
    print('what is your {0}? its {1}'.format(q, a))

for i in reversed(range(2)):
    print(i)

for i in sorted([2, 3, 4, 6, 1, 123, 34, -100]):
    print(i)
