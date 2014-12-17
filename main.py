# -*- coding: UTF-8 -*-
import sys
import traceback

import graphics
import structures
from algorithms import SweepingAlgorithm


__author__ = 'Bartosz'


class Solver(object):
    help_str = "Program usage:\n  " \
               "set_lines - set lines for solver\n  " \
               "is_crossing - check if at least one crossing occurs\n  " \
               "find_crossings - find all crossing in given lines set\n  " \
               "draw_lines - draws lines\n  " \
               "print_lines - prints lines\n  " \
               "clean - cleans list of lines\n  " \
               "help - print program usage"

    def __init__(self):
        self._algorithm = SweepingAlgorithm()
        self.lines = []

    def run(self):
        print self.help_str
        while True:
            try:
                read_text = raw_input()
                tokens = read_text.split()
                if tokens:
                    self.run_command(tokens)
            except EOFError:
                break

    def run_command(self, tokens):
        try:
            handler = getattr(self, tokens[0])
            handler(*tokens[1:])
        except AttributeError:
            traceback.print_exc()
            print 'Wrong command name:', tokens[0]
        except Exception as e:
            print 'Error: occurred', e

    def set_lines(self):
        self.clean()
        p1 = None
        win = graphics.GraphWin("", 800, 600)
        while win.isOpen():
            point = win.getMouse()
            point = structures.Point(point.x, point.y)
            if p1:
                p1.undraw()
                line = structures.Line(p1, point)
                self.lines.append(line)
                p1 = None
                line.draw(win)
            else:
                p1 = point
                p1.draw(win)

    def draw_lines(self):
        win = graphics.GraphWin("", 800, 600)
        for line in self.lines:
            line.draw(win)
        win.getMouse()
        win.close()

    def print_lines(self):
        for line in self.lines:
            print line

    def find_crossings(self):
        self._algorithm.set_lines(self.lines)
        result = self._algorithm.find_crossings()
        for point in result:
            print point

    def is_crossing(self):
        self._algorithm.set_lines(self.lines)
        print self._algorithm.is_crossing()

    def help(self):
        print self.help_str

    def clean(self):
        self.lines = []


if __name__ == '__main__':
    app = Solver()
    app.run()
    sys.exit(0)
