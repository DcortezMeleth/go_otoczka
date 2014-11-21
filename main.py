# -*- coding: UTF-8 -*-
import pickle
import traceback
import graphics

from structures import Point
from algorithms import Graham, Jarvis
from generator import Generator


__author__ = 'Bartosz'


class Solver(object):
    POINTS_FILE_NAME = "points.dat"
    RESULT_FILE_NAME = "result.dat"

    help_str = "Program usage: sage:\n  " \
               "save_points - save to file\n  " \
               "load_points - load from file\n  " \
               "save_result - save to file\n  " \
               "set_n <n> <square_n=25> <diagonal_n=20> - set number of points to generate\n  " \
               "set_range <min> <max> - set params for range generation\n  " \
               "set_circle <center.x> <center.y> <r> - set params for circle generation\n  " \
               "set_quadrilateral <x1.x> <x1.y> <x2.x> <x2.y> <x3.x> <x3.y> <x4.x> <x4.y> " \
               "- set params for quadrilateral generation\n  " \
               "set_square <x1.x> <x1.y> <x3.x> <x3.y> - set params for square generation\n  " \
               "generate <option> - generate points (0 - range, 1 - circle, 2 - quadrilateral, 3 - square)\n  " \
               "solve <algorithm> - solve problem using chosen algorithm(0 - Graham, 1 - Jarvis)\n  " \
               "print_points - print generated points\n  " \
               "print_result - prints points in result list\n  " \
               "print_help - print program usage"

    def __init__(self):
        self._generator = Generator()
        self._algorithms = {}
        self._points = []
        self._result = []

    def run(self):
        print self.help_str
        while True:
            try:
                read_text = raw_input()
                tokens = read_text.split()
                if tokens:
                    self.run_command(tokens)
            except EOFError:
                break

    def run_command(self, tokens):
        try:
            handler = getattr(self, tokens[0])
            handler(*tokens[1:])
        except AttributeError:
            traceback.print_exc()
            print 'Wrong command name:', tokens[0]
        except Exception as e:
            print 'Error: occurred', e

    def draw_points(self):
        win = graphics.GraphWin("go_otoczka", 800, 600)
        for point in self._points:
            point.draw(win)
        win.getMouse()
        win.close()

    def print_help(self):
        print self.help_str

    def print_result(self):
        print self._result

    def print_points(self):
        for point in self._points:
            print point

    def solve(self, algorithm_no):
        if not self._algorithms:
            print 'You have to generate points first!'
        algorithm = self._algorithms[int(algorithm_no)]
        algorithm.solve()
        self._result = algorithm.get_result()

    def generate(self, option):
        options = {0: self._generator.generate_range,
                   1: self._generator.generate_circle,
                   2: self._generator.generate_quadrilateral,
                   3: self._generator.generate_square}
        try:
            options[int(option)]()
            self._points = self._generator.get_points()

            self._algorithms[0] = Graham(self._points)
            self._algorithms[1] = Jarvis(self._points)
        except KeyError:
            print 'Option should be in range 0-3'

    def set_square(self, x1_x, x1_y, x3_x, x3_y):
        self._generator.set_square(Point(float(x1_x), float(x1_y)), Point(float(x3_x), float(x3_y)))

    def set_quadrilateral(self, x1_x, x1_y, x2_x, x2_y, x3_x, x3_y, x4_x, x4_y):
        self._generator.set_quadrilateral(Point(float(x1_x), float(x1_y)), Point(float(x2_x), float(x2_y)),
                                          Point(float(x3_x), float(x3_y)), Point(float(x4_x), float(x4_y)))

    def set_circle(self, x, y, r):
        self._generator.set_circle(Point(float(x), float(y)), float(r))

    def set_range(self, range_min, range_max):
        self._generator.set_range(float(range_min), float(range_max))

    def set_n(self, n, square_n=25, diagonal_n=20):
        self._generator.set_n(int(n), square_n=int(square_n), diagonal_n=int(diagonal_n))

    def save_points(self):
        pickle.dump(self._points, open(self.POINTS_FILE_NAME, 'wb'))

    def save_result(self):
        pickle.dump(self._result, open(self.RESULT_FILE_NAME, 'wb'))

    def load_points(self):
        self._generator.set_points(pickle.load(open(self.POINTS_FILE_NAME, 'rb')))


if __name__ == '__main__':
    app = Solver()
    app.run()
    sys.exit(0)