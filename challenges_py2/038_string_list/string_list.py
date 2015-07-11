#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product
import sys


def string_list(n, s):
    g = "".join(set(s))
    return sorted([''.join(k) for k in product(g, repeat=n)])


if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            n, s = test.replace("\n", "").split(",")
            results = string_list(int(n), s)
            print ",".join(results)
