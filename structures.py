# -*- coding: UTF-8 -*-
import numpy.linalg as la

__author__ = 'Bartosz'


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_equation(self):
        return [[self.x, 1], self.y]

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


class Stretch(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "[{0}, {1}]".format(str(self.a), str(self.b))

    def is_viable_crossing(self, a):
        """
        Method checks whether the crossing in point a is a viable option.

        :param a: Point
        :return: true if crossing is possible
        """
        func = lambda z, z1, z2: z1 <= z <= z2 or z2 <= z <= z1
        return func(a.x, self.a.x, self.b.x) and func(a.y, self.a.y, self.b.y)

    def get_params(self):
        a1 = [self.a.get_equation()[0], self.b.get_equation()[0]]
        b1 = [self.a.get_equation()[1], self.b.get_equation()[1]]

        # in result[0] there are a and b of our function equation
        result = la.solve(a1, b1)
        return [[result[0], -1], -result[1]]