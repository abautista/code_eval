#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Tree:
    def __init__(self, key, l, r):
        self.key = key
        self.l = l
        self.r = r


def lowest_common_ancestor(tree, a, b):
    if (a > tree.key > b) or (a < tree.key < b):
        return tree.key
    elif a > tree.key and b > tree.key:
        return lowest_common_ancestor(tree.r, a, b)
    elif a < tree.key and b < tree.key:
        return lowest_common_ancestor(tree.l, a, b)
    elif a == tree.key:
        return a
    elif b == tree.key:
        return b
    else:
        return None


t = Tree(30, Tree(8, Tree(3, None, None), Tree(20, Tree(10, None, None), Tree(29, None, None))), Tree(52, None, None))


f = open(sys.argv[1], "r")
for test_case in f:
    a, b = test_case.replace("\n", "").split(" ")
    print lowest_common_ancestor(t, int(a), int(b))

f.close()

