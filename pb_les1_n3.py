# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет действительных корней')
elif d == 0:
    print(f'Уравнение имеет единственное рещение x = {- b / (2 * a)}')
else:
    x1 = (-b + math.sqrt(d)) / 2 * a
    x2 = (-b - math.sqrt(d)) / 2 * a
    print(f'Уравнение имеет два рещениея x1 = {x1}, x2 = {x2}')
