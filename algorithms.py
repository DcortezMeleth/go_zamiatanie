# -*- coding: UTF-8 -*-
from itertools import combinations

import numpy.linalg
from numpy.linalg import LinAlgError

from structures import Point

__author__ = 'Bartosz'


# Method checks if 2 stretches are crossing.
def is_crossing(s1, s2):
    print '{0}, {1}'.format(s1, s2)
    print s1.get_params()
    print s2.get_params()

    a = [s1.get_params()[0], s2.get_params()[0]]
    b = [s1.get_params()[1], s2.get_params()[1]]

    print a
    print b

    try:
        result = numpy.linalg.solve(a, b)
        p = Point(result[0], result[1])
        return p if s1.is_viable_crossing(p) and s2.is_viable_crossing(p) else None
    except LinAlgError:
        return None


class SweepingAlgorithm(object):
    def __init__(self, stretches=None):
        if not stretches:
            stretches = []
        self._stretches = stretches
        self._result = []

    def is_crossing(self):
        if self._result:
            return True
        for pair in combinations(self._stretches, 2):
            if is_crossing(*pair):
                return True
        return False

    def find_crossings(self):
        self._result = []
        for pair in combinations(self._stretches, 2):
            p = is_crossing(*pair)
            if p:
                self._result.append([p, pair[0], pair[1]])

    def set_stretches(self, stretches):
        self._stretches = stretches

    def get_result(self):
        return self._result