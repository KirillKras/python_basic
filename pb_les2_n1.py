# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random
import math

MIN_VALUE = 1
MAX_VALUE = 10
COUNT = 10

list1 = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COUNT)]
list2 = []

for elem in list1:
    elem_sqrt = math.sqrt(elem)
    if elem_sqrt - int(elem_sqrt) == 0:
        list2.append(int(elem_sqrt))

print(list1)
print(list2)