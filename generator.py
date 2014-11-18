# -*- coding: UTF-8 -*-
import random

from structures import Point, Stretch
__author__ = 'Bartosz'


class Generator(object):

    def __init__(self, x1=0, x2=10, y1=0, y2=10):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def init_area(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def generate_point(self):
        return Point(random.uniform(self._x1, self._x2), random.uniform(self._y1, self._y2))

    def generate_stretch(self):
        return Stretch(self.generate_point(), self.generate_point())

    def generate_stretches(self, n):
        stretches = []
        for i in xrange(0, n):
            stretches.append(Stretch(self.generate_point(), self.generate_point()))