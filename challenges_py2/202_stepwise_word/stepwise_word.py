#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def make_stepwise(s):
    max_len_index = 0
    for index in range(0, len(s)):
        if len(s[index]) > len(s[max_len_index]):
            max_len_index = index

    result = ""
    for i, item in enumerate(s[max_len_index]):
        if i == 0:
            result += item
        else:
            result = result + " " + "*" * i + item
    return result

if __name__ == '__main__':

    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            s = test.replace("\n", "").split(" ")
            print make_stepwise(s)
