# -*- coding: UTF-8 -*-
from itertools import combinations

import numpy.linalg
from numpy.linalg import LinAlgError

from structures import Point, BinaryTree

__author__ = 'Bartosz'


# Method checks if 2 stretches are crossing.
def are_crossing(s1, s2):
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
            s = point.line
            if point == s.left:
                self._broom.insert(s)
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1 and are_crossing(s, s1):
                    return True
                if s2 and are_crossing(s, s2):
                    return True
            else:
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1 and s2 and are_crossing(s1, s2):
                    return True
                self._broom.remove(s)
        return False

    def find_crossings(self):
        self._result = []
        for pair in combinations(self._lines, 2):
            p = are_crossing(*pair)
            if p:
                self._result.append([p, pair[0], pair[1]])

    def set_lines(self, lines):
        self._lines = lines
        points = []
        for line in lines:
            points.extend([line.p1, line.p2])
        self._points = sorted(points, key=lambda p: p.x)
        for po in self._points:
            print po, po.x, po.y

    def get_result(self):
        return self._result