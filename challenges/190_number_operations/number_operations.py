#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from itertools import permutations


def check(l):
    number = l[0]
    l = l[1:]
    if len(l) == 0:
        if number == 42:
            return True
        else:
            return False
    else:
        second_number = l.pop()
        t1 = [number + second_number] + l
        t2 = [number - second_number] + l
        t3 = [number * second_number] + l
        return check(t1) or check(t2) or check(t3)


def check_all(l):
    for p in permutations(l):

        if check(list(p)):
            return True

    return False

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test = test.replace("\n", "").split(" ")
            test = [int(t) for t in test]

            if check_all(test):
                print "YES"
            else:
                print "NO"
