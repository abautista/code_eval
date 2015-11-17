#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def get_subordinates(boss, pairs):
    subordinates = []
    filtered_pairs = filter(lambda p: p[0] == boss, pairs)
    first_order_subordinates = sorted(map(lambda p: p[1], filtered_pairs))

    for subordinate in first_order_subordinates:
        subordinates.append((subordinate, get_subordinates(subordinate, pairs)),)
    return subordinates


def make_hierarchy(pairs):
    managers = [x[0] for x in pairs]
    subordinates = sorted([x[1] for x in pairs])
    boss = [x for x in managers if x not in subordinates][0]

    return (boss, get_subordinates(boss, pairs))


def printed_hierarchy(hierarchy):
    if len(hierarchy) == 0:
        return ""
    if len(hierarchy[1]) == 0:
        return hierarchy[0]

    subordinates = []
    for subordinate in hierarchy[1]:
        subordinates.append(printed_hierarchy(subordinate))

    return hierarchy[0] + " [" + ", ".join(subordinates) + "]"

if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            pairs = test.replace("\n", "").split(" | ")
            pairs = [(pair[0], pair[1]) for pair in pairs]
            print printed_hierarchy(make_hierarchy(pairs))
