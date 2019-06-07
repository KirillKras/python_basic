# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random

MIN_VALUE = 1
MAX_VALUE = 10
COUNT = 10

list1 = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COUNT)]
list2 = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COUNT)]

for elem in set(list1):
    if elem in list2:
        list2.remove(elem)

print(list2)