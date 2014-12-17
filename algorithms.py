# -*- coding: UTF-8 -*-

import numpy.linalg
from numpy.linalg import LinAlgError
import graphics

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

    def in_result(self, point2):
        for point in self._result:
            if point.swap[0] in point2.swap and point.swap[1] in point2.swap:
                return True
        return False

    def callback(self, point):
        if not self.in_result(point):
            self._result.append(point)
            self.add_point(point)
            point.swap[0].setFill('red')
            point.swap[1].setFill('red')

    def find_crossings(self):
        win = graphics.GraphWin("go_zamiatanie", 800, 600)
        for line in self._lines:
            line.draw(win)
        for point in self._points:
            self._broom.x = point.x
            broom = graphics.Line(graphics.Point(point.x, 0), graphics.Point(point.x, 600))
            broom.setFill('green')
            broom.draw(win)
            s = point.line
            # gdy to przeciecie
            if point.swap:
                self._broom.swap(*point.swap)
                if self._broom.lines.index(point.swap[0]) > self._broom.lines.index(point.swap[1]):
                    point.swap[0], point.swap[1] = point.swap[1], point.swap[0]
                s1 = self._broom.prev(point.swap[0])
                s2 = self._broom.next(point.swap[1])
                if s1:
                    cross = are_crossing(point.swap[0], s1)
                    if cross:
                        self.callback(cross)
                if s2:
                    cross = are_crossing(point.swap[1], s2)
                    if cross:
                        self.callback(cross)
            # = gdy to poczatek odcinka
            elif point == s.left:
                self._broom.insert(s)
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1:
                    cross = are_crossing(s, s1)
                    if cross:
                        self.callback(cross)
                if s2:
                    cross = are_crossing(s, s2)
                    if cross:
                        self.callback(cross)
            # gdy koniec odcinka
            else:
                s1 = self._broom.prev(s)
                s2 = self._broom.next(s)
                if s1 and s2:
                    cross = are_crossing(s1, s2)
                    if cross:
                        self.callback(cross)
                self._broom.remove(s)
            win.getMouse()
            broom.undraw()
        win.getMouse()
        win.close()
        return self._result

    def add_point(self, point):
        i = 0
        while self._points[i].x < point.x:
            i += 1
        self._points.insert(i, point)

    def set_lines(self, lines):
        self._lines = lines
        points = []
        for line in lines:
            points.extend([line.left, line.right])
        self._points = sorted(points, key=lambda p: p.x)