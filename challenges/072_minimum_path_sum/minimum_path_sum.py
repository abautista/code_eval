#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def minimum_path_sum(m, i, j):
    n = len(m)
    if i == n-1 and j == n-1:
        return m[i][j]
    elif i == n-1 and j < n-1:
        return m[i][j] + minimum_path_sum(m, i, j+1)
    elif j == n-1 and i < n-1:
        return m[i][j] + minimum_path_sum(m, i+1, j)
    else:
        return m[i][j] + min(minimum_path_sum(m, i, j+1), minimum_path_sum(m, i+1, j))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        rows_number = f.readline()
        while rows_number:
            matrix = []
            for i in range(0, int(rows_number)):
                row = f.readline().replace("\n", "").split(",")
                row = [int(x) for x in row]
                matrix.append(row)
            print minimum_path_sum(matrix, 0, 0)
            rows_number = f.readline()
