#!/usr/bin/env python
# -*- coding: utf-8 -*-


from functools import wraps
import sys


def memoize(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            print fib(int(test))
