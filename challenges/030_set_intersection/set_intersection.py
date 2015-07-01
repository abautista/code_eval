#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def compute_intersection(l):
    lists = l.replace("\n", "").split(";")
    components1 = lists[0].split(",")
    components2 = lists[1].split(",")
    result = []
    
    for number in components1:
        for number_2 in components2:
            if number == number_2:
               result.append(number)

            if number_2 > number:
                break;

    print ",".join(result)


if __name__ == '__main__':

    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            compute_intersection(test)
