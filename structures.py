# -*- coding: UTF-8 -*-
__author__ = 'Bartosz'
import numpy.linalg as la
import graphics


# klasa reprezentująca punkt w przestrzeni
class Point(graphics.Point):
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


# klasa reprezentująca prosta
class Line(object):
    def __init__(self, a, b, c=1, x1=None, x2=None):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = x1
        self.x2 = x2

    def __str__(self):
        return "[{0}, {1}]".format(str(self.a), str(self.b))

    def delta_x(self):
        return abs(self.x1.x - self.x2.x)

    def delta_y(self):
        return abs(self.x1.y - self.x2.y)

    def get_lower_x(self):
        return self.x1.x if self.x1.x < self.x2.x else self.x2.x

    def get_lower_y(self):
        return self.x1.y if self.x1.y < self.x2.y else self.x2.y

    def is_ok(self):
        return self.c != 0

    def get_y(self, x):
        return (self.a * x + self.b) / self.c

    @staticmethod
    def get_line(x1, x2):
        m1 = [[x1.x, 1], [x2.x, 1]]
        m2 = [x1.y, x2.y]
        try:
            result = la.solve(m1, m2)
            return Line(result[0], result[1], x1=x1, x2=x2)
        # przypadek gdy układ równań liniowo zależnych - prosta prostopadła do ox
        except la.LinAlgError:
            return Line(x1.x, 0, c=0, x1=x1, x2=x2)
