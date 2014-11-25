# -*- coding: UTF-8 -*-
from itertools import combinations

import numpy.linalg
from numpy.linalg import LinAlgError

from structures import Point, BinaryTree

__author__ = 'Bartosz'


# Method checks if 2 stretches are crossing.
def is_crossing(s1, s2):
    a = [s1.get_params()[0], s2.get_params()[0]]
    b = [s1.get_params()[1], s2.get_params()[1]]

    try:
        result = numpy.linalg.solve(a, b)
        p = Point(result[0], result[1])

        return p if s1.is_viable_crossing(p) and s2.is_viable_crossing(p) else None
    except LinAlgError:
        return None


class SweepingAlgorithm(object):
    def __init__(self):
        self._lines = []
        self._points = []
        self._broom = BinaryTree()
        self._result = []

    def is_crossing(self):
        for point in self._points:
            if point == point.line.left:
                self._broom.insert(point)
                s1 = self._broom.prev(point)
                s2 = self._broom.next(point)
                if s1 and is_crossing(point.line, s1.line):
                    return True
                if s2 and is_crossing(point.line, s2.line):
                    return True
            else:
                s1 = self._broom.prev(point)
                s2 = self._broom.next(point)
                if s1 and s2 and is_crossing(s1.line, s2.line):
                    return True
        return False

    def find_crossings(self):
        self._result = []
        for pair in combinations(self._lines, 2):
            p = is_crossing(*pair)
            if p:
                self._result.append([p, pair[0], pair[1]])

    def set_lines(self, lines):
        self._lines = lines
        points = []
        for line in lines:
            points.extend([line.p1, line.p2])
        self._points = sorted(points, key=lambda p: p.x)

    def get_result(self):
        return self._result