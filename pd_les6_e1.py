# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.



import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b ,c):

        def lineside(point1, point2):
            return math.sqrt((point2.x - point1.x) ** 2
                             + (point2.y - point1.y) ** 2)

        self.a = a
        self.b = b
        self.c = c

        self.ab = lineside(a, b)
        self.bc = lineside(b, c)
        self.ac = lineside(a, c)

    def perimeterTrianger(self):
        return self.ab + self.bc + self.ac

    def areaTriangle(self):
        semi_perimeter = self.perimeterTrianger() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.ab) *
                         (semi_perimeter - self.bc) * (semi_perimeter - self.ac))


triangle = Triangle(Point(3, 2), Point(6, 7), Point(0, 12))