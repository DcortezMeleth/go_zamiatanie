# -*- coding: UTF-8 -*-
import numpy.linalg as la

__author__ = 'Bartosz'


class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def get_equation(self):
        return [[self._x, 1], self._y]


class Stretch(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def is_viable_crossing(self, a):
        """
        Method checks whether the crossing in point a is a viable option.

        :param a: Point
        :return: true if crossing is possible
        """
        func = lambda z, z1, z2: z1 <= z <= z2 or z2 <= z <= z1
        return func(a.x(), self._a.x(), self._b.x()) and func(a.y(), self._a.y(), self._b.y())

    def get_params(self):
        a = [self._a.get_equation()[0], self._b.get_equation()[0]]
        b = [self._a.get_equation()[1], self._b.get_equation()[1]]

        # in result[0] there are a and b of our function equation
        result = la.solve(a, b)
        return [[result[0], -1], result[1]]