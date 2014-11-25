# -*- coding: UTF-8 -*-
import numpy.linalg as la
import graphics

__author__ = 'Bartosz'


class BinaryTree(object):
    def __init__(self):
        pass

    def insert(self, a):
        pass

    def remove(self, a):
        pass

    def next(self, a):
        pass

    def prev(self, a):
        pass


class Point(graphics.Point):
    def __init__(self, x, y):
        graphics.Point.__init__(self, x, y)
        self.line = None
        self.side = None

    def get_equation(self):
        return [[self.x, 1], self.y]

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


class Line(graphics.Line):
    def __init__(self, p1, p2):
        p1.line = self
        p2.line = self
        if p1.x > p2.x:
            p1, p2 = p2, p1
        self.left = p1
        self.right = p2
        graphics.Line.__init__(self, p1, p2)

    def __str__(self):
        return "[{0}, {1}]".format(str(self.p1), str(self.p2))

    def is_viable_crossing(self, a):
        """
        Method checks whether the crossing in point a is a viable option.

        :param a: Point
        :return: true if crossing is possible
        """
        func = lambda z, z1, z2: z1 <= z <= z2 or z2 <= z <= z1
        return func(a.x, self.p1.x, self.p2.x) and func(a.y, self.p1.y, self.p2.y)

    def get_params(self):
        a1 = [self.p1.get_equation()[0], self.p2.get_equation()[0]]
        b1 = [self.p1.get_equation()[1], self.p2.get_equation()[1]]

        # in result[0] there are a and b of our function equation
        result = la.solve(a1, b1)
        return [[result[0], -1], -result[1]]