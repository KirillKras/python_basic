# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

MIN_VALUE = 1
MAX_VALUE = 10
COUNT = 10

list1 = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COUNT)]

print(list(set(list1)))

d = {}

for elem in list1:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

print([k for k, v in d.items() if v == 1])