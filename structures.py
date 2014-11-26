# -*- coding: UTF-8 -*-
import numpy.linalg as la
import graphics

__author__ = 'Bartosz'


class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None

    def is_lower(self, node):
        return node.val.x > self.val.x

    def is_higher(self, node):
        return node.val.x < self.val.x

    def is_equal(self, node):
        return self.val.x == node.val.x and self.val.y == node.val.y


class BinaryTree(object):
    def __init__(self):
        self._root = None

    def insert(self, val):
        node = Node(val)
        if not self._root:
            self._root = node
            return
        tmp = self._root
        while True:
            if node.is_lower(tmp):
                if not tmp.left:
                    node.parent = tmp
                    tmp.left = node
                    return
                tmp = tmp.left
            else:
                if not tmp.right:
                    node.parent = tmp
                    tmp.right = node
                    return
                tmp = tmp.right

    def remove(self, val):
        node = Node(val)
        tmp = self._root
        while not tmp.is_equal(node):
            if node.is_lower(tmp):
                if not tmp.left:
                    raise Exception("Elem not found!")
                tmp = tmp.left
            else:
                if not tmp.right:
                    raise Exception("Elem not found!")
                tmp = tmp.right
        #TODO:tu cos z tym zrobic!!!
        if tmp.left:
            tmp.left.parent = tmp.parent
            tmp = tmp.left
        elif tmp.right:
            tmp.right.parent = tmp.parent
            tmp = tmp.right
        else:
            tmp

    def next(self, a):
        pass

    def prev(self, a):
        pass


class Point(graphics.Point):
    def __init__(self, x, y):
        graphics.Point.__init__(self, x, y)
        self.line = None
        self.side = None

    def get_equation(self):
        return [[self.x, 1], self.y]

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


class Line(graphics.Line):
    def __init__(self, p1, p2):
        p1.line = self
        p2.line = self
        if p1.x > p2.x:
            p1, p2 = p2, p1
        self.left = p1
        self.right = p2
        graphics.Line.__init__(self, p1, p2)

    def __str__(self):
        return "[{0}, {1}]".format(str(self.p1), str(self.p2))

    def is_viable_crossing(self, a):
        """
        Method checks whether the crossing in point a is a viable option.

        :param a: Point
        :return: true if crossing is possible
        """
        func = lambda z, z1, z2: z1 <= z <= z2 or z2 <= z <= z1
        return func(a.x, self.p1.x, self.p2.x) and func(a.y, self.p1.y, self.p2.y)

    def get_params(self):
        a1 = [self.p1.get_equation()[0], self.p2.get_equation()[0]]
        b1 = [self.p1.get_equation()[1], self.p2.get_equation()[1]]

        # in result[0] there are a and b of our function equation
        result = la.solve(a1, b1)
        return [[result[0], -1], -result[1]]