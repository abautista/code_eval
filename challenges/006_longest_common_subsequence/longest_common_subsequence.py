#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import combinations


def lcs_brute(r, s):
    for length in range(len(s), 0, -1):
        for subsequence_r in combinations(r, length):
            for subsequence_s in combinations(s, length):
                if subsequence_r == subsequence_s:
                    return ''.join(subsequence_r)


def lcs_table(r, s):
    table = [[0 for j in range(0, len(s)+1)]]
    for i in range(1, len(r)+1):
        row = [0]
        for j in range(1, len(s)+1):
            if r[i-1] == s[j-1]:
                result = table[i-1][j-1] + 1
            else:
                result = max(table[i-1][j], row[j-1])
            row.append(result)
        table.append(row)
    return table


def assemble_lcs(r, s, table, i, j):

    if table[i][j] == 0:
        return ""

    if r[i-1] == s[j-1]:
        return assemble_lcs(r, s, table, i-1, j-1) + r[i-1]
    else:
        if table[i][j-1] > table[i-1][j]:
            return assemble_lcs(r, s, table, i, j-1)
        else:
            return assemble_lcs(r, s, table, i-1, j)


def print_table(table):
    for row in table:
        print row

if __name__ == '__main__':

    with open(sys.argv[1]) as test_cases:
        for test in test_cases:
            r, s = test.replace("\n", "").split(";")
            table = lcs_table(r, s)
            result = assemble_lcs(r, s, table, len(r), len(s))
            print result
