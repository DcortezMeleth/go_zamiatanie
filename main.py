# -*- coding: UTF-8 -*-
from generator import Generator
from structures import Stretch, Point

__author__ = 'Bartosz'

import sys
import pickle


class Solver(object):
    FILE_NAME = "stretches.dat"

    def __init__(self):
        self._stretches = []
        self._generator = Generator()

    def run(self):
        print "Remember to create or get account at the beginning. Usage:\n " \
              "save_stretches - save to file\n " \
              "load_stretches - load from file\n " \
              "set_generator_area <x1> <x2> <y1> <y2> - set area for stretches generator\n " \
              "generate_stretches <n> - generate n stretches\n " \
              "add_stretch <x1> <y1> <x2> <y2> - add stretch between 2 points\n " \
              "clean - cleans list of stretches"
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
            print 'Wrong command name:', tokens[0]
        except Exception as e:
            print 'Error: occurred', e

    def save_stretches(self, ):
        pickle.dump(self._stretches, self.FILE_NAME)

    def load_stretches(self):
        self._stretches = pickle.load(self.FILE_NAME)

    def set_generator_area(self, x1, x2, y1, y2):
        self._generator.init_area(x1, x2, y1, y2)

    def generate_stretches(self, n):
        self._stretches = self._generator.generate_stretches(n)

    def add_stretch(self, x1, y1, x2, y2):
        self._stretches.append(Stretch(Point(x1, y1), Point(x2, y2)))

    def clean(self):
        self._stretches = []


if __name__ == '__main__':
    app = Solver()
    app.run()
    sys.exit(0)