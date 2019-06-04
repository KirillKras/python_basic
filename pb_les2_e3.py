# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random

MIN_VALUE = 1
MAX_VALUE = 10
COUNT = 10

list1 = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COUNT)]
list2 = []

for elem in list1:
    if elem % 2 == 0:
        list2.append(elem / 4)
    else:
        list2.append(elem * 2)

print(list1)
print(list2)