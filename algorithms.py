# -*- coding: UTF-8 -*-
import math
import traceback

__author__ = 'Bartosz'


# metoda licząca kąt pomiędzy punktami
def get_degree(base, target):
    angle = math.degrees(math.atan2(target.y - base.y, target.x - base.x))
    if angle < 0:
        angle += 360
    return angle


# metoda licząca kąt pomiędzy punktami dla odwróconej osi x
def get_degree_reverse(base, target):
    angle = math.degrees(math.atan2(target.y - base.y, base.x - target.x))
    if angle < 0:
        angle += 360
    return angle


# metoda licząca dystans pomiędzy punktami
def get_distance(base, target):
    return math.sqrt((base.x - target.x) ** 2 + (base.y - target.y) ** 2)


# wyszukuje w liście punkt o najmniejszym y
def find_lowest_y(points):
    lowest = points[0]
    for point in points:
        if point.y < lowest.y or point.y == lowest.y and point.x < lowest.x:
            lowest = point
    return lowest


# wyszukuje w liście punkt o największym y
def find_highest_y(points):
    highest = points[0]
    for point in points:
        if point.y > highest.y or point.y == highest.y and point.x < highest.x:
            highest = point
    return highest


# sprawdza czy punkt z leży na lewo od odcinka [x,y]
def is_left(x, y, z):
    alpha = get_degree(x, y)
    beta = get_degree(x, z)
    return alpha < beta < alpha + 180


class Graham(object):
    def __init__(self, points):
        self._points = points
        self._p0 = find_lowest_y(points)
        self._result = []

    def solve(self):
        if len(self._points) < 3:
            return None

        # krok pierwszy - wybieramy p0 - zrobione w konstruktorze

        # krok drugi - sortowanie punktów
        sorted_points = sorted(self._points, key=lambda x: (get_degree(self._p0, x), -get_distance(self._p0, x)))
        result = [sorted_points[0]]
        for point in sorted_points[1:]:
            if get_degree(self._p0, point) != get_degree(self._p0, result[-1]):
                result.append(point)

        # krok trzeci - definiujemy stos
        self._result = result[:3]

        # krok czwarty - szukanie rozwiązania
        i = 3
        while i < len(result):
            if is_left(self._result[-2], self._result[-1], result[i]):
                self._result.append(result[i])
                i += 1
            else:
                self._result.pop()

    def get_result(self):
        return self._result


class Jarvis(object):
    def __init__(self, points):
        self._points = points
        self._p0 = find_lowest_y(points)
        self._p1 = find_highest_y(points)
        self._result = []

    def solve(self):
        if len(self._points) < 3:
            return None

        # prawa strona otoczki
        tmp = self._p0
        while tmp != self._p1:
            sorted_points = sorted(self._points, key=lambda x: (get_degree(tmp, x), -get_distance(tmp, x)))
            # pierwszym elementem zawsze będzie nasz obecny punkt, bo mamy wtedy kąt 0 stopni
            self._result.append(sorted_points[1])
            tmp = self._result[-1]

        # lewa strona otoczki
        while tmp != self._p1:
            sorted_points = sorted(self._points, key=lambda x: (get_degree_reverse(tmp, x), -get_distance(tmp, x)))
            self._result.append(sorted_points[1])
            tmp = self._result[-1]

        # usuwamy p1, bo zostało dodane 2 razy
        self._result = self._result[:-1]

    def get_result(self):
        return self._result