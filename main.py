# -*- coding: UTF-8 -*-
import sys
import pickle
import traceback
import json
import graphics
import structures

from algorithms import SweepingAlgorithm


__author__ = 'Bartosz'


class Solver(object):
    FILE_NAME = "stretches.dat"
    RESULT_FILE_NAME = "result.dat"

    help_str = "Program usage:\n " \
               "save_stretches - save to file\n  " \
               "load_stretches - load from file\n  " \
               "set_generator_area <x1> <x2> <y1> <y2> - set area for stretches generator\n  " \
               "generate_stretches <n> - generate n stretches\n  " \
               "add_stretch <x1> <y1> <x2> <y2> - add stretch between 2 points\n  " \
               "clean - cleans list of stretches\n  " \
               "print_stretches - prints stretches\n  " \
               "is_crossing - check if at least one crossing occurs\n  " \
               "find_crossings - find all crossing in given stretches set\n  " \
               "save_result - saves result to file\n  " \
               "print_help - show program usage\n  " \
               "draw_stretches - draws stretches\n  " \
               "draw_result - draws result of sweeping algorithm"

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

    def find_crossings(self):
        self._algorithm.set_lines(self.lines)
        self._algorithm.find_crossings()
        for elem in self._algorithm.get_result():
            print "Point: {0} Stretches: {1} {2}".format(*elem)

    def is_crossing(self):
        self._algorithm.set_lines(self.lines)
        # print self._algorithm.is_crossing()

    def add_stretch(self, x1, y1, x2, y2):
        self.lines.append(Stretch(Point(float(x1), float(y1)), Point(float(x2), float(y2))))

    def help(self):
        print self.help_str

    def clean(self):
        self.lines = []


if __name__ == '__main__':
    app = Solver()
    app.run()
    sys.exit(0)
