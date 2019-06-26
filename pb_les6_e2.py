# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Trapeze:

    def __init__(self, a, b, c, d):
        def lineside(point1, point2):
            return math.sqrt((point2.x - point1.x) ** 2
                             + (point2.y - point1.y) ** 2)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = lineside(a, b)
        self.bc = lineside(b, c)
        self.cd = lineside(c, d)
        self.da = lineside(d, a)
        self.ac = lineside(a, c)
        self.bd = lineside(b, d)

    @property
    def trapeze_perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    @property
    def trapeze_square(self):
        perimeter_triangel1 = 0.5 * (self.ab + self.bc + self.ac)
        perimeter_triangel2 = 0.5 * (self.cd + self.da + self.ac)
        square1 = math.sqrt(perimeter_triangel1 * (perimeter_triangel1 - self.ab) *
                         (perimeter_triangel1 - self.bc) * (perimeter_triangel1 - self.ac))
        square2 = math.sqrt(perimeter_triangel2 * (perimeter_triangel2 - self.cd) *
                            (perimeter_triangel2 - self.da) * (perimeter_triangel2 - self.ac))
        return square1 + square2

    def isTrapezeEqu(self):
        return self.ac == self.bd
