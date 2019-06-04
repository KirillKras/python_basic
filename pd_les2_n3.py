# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

MIN_VALUE = -100
MAX_VALUE = 100
COUNT = 100

list1 = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COUNT)]

print(list1)