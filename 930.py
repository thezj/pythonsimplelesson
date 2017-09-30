list1 = [1, 2, 3]
list1.append(4)
del list1[3]
list1.remove(1)
print(list1, len(list1), list1 + [4, 5], list1 * 2, 4 in list1)

for list1item in list1:
    print(list1item)

print(list1)

list2 = list((1, 2, 3))
print(list2, list2.count(3), list2.extend((4, 5)), list2)
print(list2.index(3))
list2.insert(5, 6)
print(list2, list2.pop(), list2)
list2.remove(3)
print(list2)
list2.reverse()
print(list2)
list2.sort()
print(list2)
# list2.clear()
list3 = list2.copy()
print(list3,list2,list3 is list2,list3 == list2)
