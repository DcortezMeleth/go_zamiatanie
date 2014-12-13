# -*- coding: UTF-8 -*-
from itertools import combinations

import numpy.linalg
from numpy.linalg import LinAlgError

import structures

__author__ = 'Bartosz'


# Method checks if 2 stretches are crossing.
def are_crossing(s1, s2):
    a = [s1.get_params()[0], s2.get_params()[0]]
    b = [s1.get_params()[1], s2.get_params()[1]]

    try:
        result = numpy.linalg.solve(a, b)
        p = structures.Point(result[0], result[1])
        p.swap = [s1, s2]
        return p if s1.is_viable_crossing(p) and s2.is_viable_crossing(p) else None
    except LinAlgError:
        return None


class SweepingAlgorithm(object):
    def __init__(self):
        self._lines = []
        self._points = []
        self._broom = structures.Broom()
        self._result = []

    def is_crossing(self):
        for point in self._points:
            self._broom.x = point.x
            s = point.line
            # = gdy to poczatek odcinka
            if point == s.left:
                self._broom.insert(s)
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1 and are_crossing(s, s1):
                    return True
                if s2 and are_crossing(s, s2):
                    return True
            # gdy koniec odcinka
            else:
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1 and s2 and are_crossing(s1, s2):
                    return True
                self._broom.remove(s)
        return False

    def find_crossings(self):
        for point in self._points:
            self._broom.x = point.x
            s = point.line
            # = gdy to poczatek odcinka
            if point.swap:
                self._broom.swap(*point.swap)
            elif point == s.left:
                self._broom.insert(s)
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1:
                    cross = are_crossing(s, s1)
                    if cross:
                        self._result.append(cross)
                        self.add_point(cross)
                if s2:
                    cross = are_crossing(s, s2)
                    if cross:
                        self._result.append(cross)
                        self.add_point(cross)
            # gdy koniec odcinka
            else:
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1 and s2:
                    cross = are_crossing(s1, s2)
                    if cross:
                        self._result.append(cross)
                        self.add_point(cross)
                self._broom.remove(s)
        return self._result

    def add_point(self, point):
        i = 0
        while self._points.x < point.x:
            i += 1
        self._points.insert(i, point)

    def set_lines(self, lines):
        self._lines = lines
        points = []
        for line in lines:
            points.extend([line.left, line.right])
        self._points = sorted(points, key=lambda p: p.x)
        for point in self._points:
            print point