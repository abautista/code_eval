#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def mth_element(line):
    line.replace("\n", "")
    tokens = line.split(" ")
    index = tokens[-1]
    tokens = tokens[:len(tokens)-1]

    if int(index) > len(tokens):
        return

    print tokens[len(tokens) - int(index)]


if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for line in test_cases:
            mth_element(line)
