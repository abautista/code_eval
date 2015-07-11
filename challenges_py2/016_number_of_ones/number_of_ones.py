#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def count_ones(number):
    number_of_ones = 0
    result, remainder = divmod(number, 2)
    if remainder == 1:
        number_of_ones += 1

    while result != 0:
        result, remainder = divmod(result, 2)
        if remainder == 1:
            number_of_ones += 1
    return number_of_ones

if __name__ == '__main__':

    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            print count_ones(int(test.replace("\n", "")))
