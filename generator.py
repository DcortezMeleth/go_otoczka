# -*- coding: UTF-8 -*-
import random
import math

from structures import Point, Line


__author__ = 'Bartosz'


class Generator(object):
    def __init__(self, n=100):
        # opcja i ilość punktów do wygenerowania
        self._n = n
        self._square_n = 25
        self._diagonal_n = 20
        # granice przedziału
        self._min = -100
        self._max = 100
        # środek i promień okręgu
        self._center = Point(0, 0)
        self._r = 10
        # 4 wierzchołki czworokąta
        self._quadra = [Point(-10, 10), Point(-10, -10), Point(10, -10), Point(10, 10)]
        # 2 wierzchołki jednoznacznie wyznaczające kwadrat
        self._square = [Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)]
        # cache ostatnio wygenerowanych punktów
        self._generated = []

    def set_n(self, n, square_n=25, diagonal_n=20):
        self._n = n
        self._square_n = square_n
        self._diagonal_n = diagonal_n

    def set_range(self, range_min, range_max):
        self._min = range_min
        self._max = range_max

    def set_circle(self, center, r):
        self._center = center
        self._r = r

    def set_quadrilateral(self, a, b, c, d):
        self._quadra = [a, b, c, d]

    # x1 i x2 to dwa przeciwległe wierzchołki kwadratu
    def set_square(self, x1, x3):
        self._square = [x1, Point(x1.x, x3.y), x3, Point(x3.x, x1.y)]

    def get_points(self):
        return self._generated

    def set_points(self, points):
        self._generated = points

    # generowanie punktów w zadanym przedziale
    def generate_range(self):
        result = []
        for i in xrange(0, self._n):
            x = (self._max - self._min) * random.random() + self._min
            y = (self._max - self._min) * random.random() + self._min
            result.append(Point(x, y))
        self._generated = result
        return result

    # generowanie punktów leżących na okręgu
    def generate_circle(self):
        result = []
        for i in xrange(0, self._n):
            t = 2.0 * math.pi * random.random()
            x = self._center.x + self._r * math.cos(t)
            y = self._center.y + self._r * math.sin(t)
            result.append(Point(x, y))
        self._generated = result
        return result

    # generowanie punktów leżących na bokach czworokąta
    def generate_quadrilateral(self, n=None, quadra=None):
        if not n:
            n = self._n
        if not quadra:
            quadra = self._quadra
        result = []
        for i in xrange(0, n):
            # losujemy 2 punkty leżące na jednym boku
            idx = random.randint(0, 3)
            x1 = quadra[idx]
            x2 = quadra[idx + 1] if idx != 3 else quadra[0]

            line = Line.get_line(x1, x2)
            x = line.delta_x() * random.random() + line.get_lower_x()

            # jeśli jest to normalna funkcja liczymy y z wzoru f(x) = ax + b
            if line.is_ok():
                y = line.get_y(x)
            # w przeciwnym wypadku losujemy położenie y pomiędzy dwoma punktami
            else:
                y = line.delta_y() * random.random() + line.get_lower_y()
            result.append(Point(x, y))
        self._generated = result
        return result

    def generate_square(self):
        result = []
        for i in xrange(0, self._diagonal_n):
            idx = random.randint(0, 1)
            line = Line.get_line(self._square[idx], self._square[idx + 2])
            x = line.delta_x() * random.random() + line.get_lower_x()
            y = line.get_y(x)
            result.append(Point(x, y))
        # kwadrat jest czworokątem, więc punkty na nim generujemy z napisanej już metody
        result.extend(self.generate_quadrilateral(n=self._square_n, quadra=self._square))
        self._generated = result
        return result
