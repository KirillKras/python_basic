# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import re

def get_number(number):
    d_number = {
        'positive': 1,
        'numerator': None,
        'denominator': 1
    }
    znak = 1
    if '-' in number:
        znak = -1
        number = number.replace('-', '')
    if ' ' in number:
        integer, fraction = number.split(' ')
        d_number['numerator'], d_number['denominator'] = map(int, fraction.split('/'))
        d_number['numerator'] += int(integer) * d_number['denominator']
    elif '/' in number:
        d_number['numerator'], d_number['denominator'] = map(int, number.split('/'))
    else:
        d_number['numerator'] = int(number)
    if znak == -1:
        d_number['numerator'] = -1 * d_number['numerator']
    return d_number


def get_simple(numerator, denomerator):
    for i in range(numerator, 2, -1):
        if (numerator % i == 0) and (denomerator % i == 0):
            return numerator // i, denomerator // i
    return numerator, denomerator


def operation(d_number1, d_number2, operand):
    znak = 1
    numerator = d_number1['numerator'] * d_number2['denominator'] + \
                d_number2['numerator'] * d_number1['denominator'] * operand
    denominator = d_number1['denominator'] * d_number2['denominator']
    if numerator < 0:
        znak = -1
        numerator = abs(numerator)
    integer = abs(numerator) // denominator
    numerator = numerator % denominator
    numerator, denominator = get_simple(numerator, denominator)
    return znak, integer, numerator, denominator


def printer(znak, integer, numerator, denominator):
    if integer and numerator:
        return f'{znak*integer} {numerator}/{denominator}'
    elif integer:
        return f'{znak*integer}'
    elif numerator:
        return f'{znak*numerator}/{denominator}'
    else:
        return '0'

expression = input('Введите выражение для вычисления: ')

if ' + ' in expression:
    number1, number2 = expression.split(' + ')
    operand = 1
else:
    number1, number2 = expression.split(' - ')
    operand = -1

d_number1 = get_number(number1)
d_number2 = get_number(number2)

znak, integer, numerator, denominator = operation(d_number1, d_number2, operand)
result = printer(znak, integer, numerator, denominator)
print(result)