# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# вычислите и выведите y

equation = input('Введите уравнение прямой: ')
x = float(input('Введите значение x: '))

equation_x = equation.split('x')

k = float(equation_x[0].split('=')[1])

if '+' in equation_x[1]:
    b = float(equation_x[1].split('+')[1])
else:
    b = - float(equation_x[1].split('-')[1])

print(f'y = {k * x + b}')