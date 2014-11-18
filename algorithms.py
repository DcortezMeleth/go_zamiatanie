# -*- coding: UTF-8 -*-
from itertools import combinations

import numpy.linalg
from numpy.linalg import LinAlgError

from structures import Point

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
    def __init__(self, stretches):
        self._stretches = stretches
        self._result = []

    def run(self):
        for pair in combinations(self._stretches, 2):
            is_crossing(*pair)