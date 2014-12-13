# -*- coding: UTF-8 -*-
import numpy.linalg as la
import graphics

__author__ = 'Bartosz'
# TODO: Napisac na SO, dlaczego z tym Point tak dziwnie to dziala


class Point(graphics.Point):
    def __init__(self, x, y):
        graphics.Point.__init__(self, x, y)
        self.line = None
        self.side = None
        self.swap = []

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def get_equation(self):
        return [[self.x, 1], self.y]


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
        return "[{0}, {1}]".format(str(self.left), str(self.right))

    def get_y(self, x):
        a = self.get_params()[0][0]
        b = self.get_params()[1]
        return a*x + b

    def is_viable_crossing(self, a):
        func = lambda z, z1, z2: z1 <= z <= z2 or z2 <= z <= z1
        return func(a.x, self.p1.x, self.p2.x) and func(a.y, self.p1.y, self.p2.y)

    def get_params(self):
        a1 = [self.left.get_equation()[0], self.right.get_equation()[0]]
        b1 = [self.left.get_equation()[1], self.right.get_equation()[1]]

        # in result[0] there are a and b of our function equation
        result = la.solve(a1, b1)
        return [[result[0], -1], -result[1]]


class Broom(object):
    def __init__(self):
        self.lines = []
        self.x = 0

    def swap(self, s1, s2):
        i1, i2 = self.lines.index(s1), self.lines.index(s2)
        self.lines[i1], self.lines[i2] = self.lines[i2], self.lines[i1]

    def insert(self, s):
        y = s.get_y(self.x)
        i = 0
        while self.lines[i].get_y(self.x) > y:
            i += 1
        self.lines.insert(i, s)

    def remove(self, s):
        self.lines.remove(s)

    def next(self, s):
        return self.lines[self.lines.index(s) + 1]

    def prev(self, s):
        return self.lines[self.lines.index(s) - 1]