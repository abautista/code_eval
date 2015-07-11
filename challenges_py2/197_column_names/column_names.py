#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from string import ascii_uppercase


mappings = dict(zip(range(0, 26), ascii_uppercase))


def compute_column_header(column_number):
    column_header = ""
    div, mod = divmod(column_number-1, 26)
    while div != 0:
        column_header = mappings[mod] + column_header
        div, mod = divmod(div-1, 26)
    column_header = mappings[mod] + column_header
    return column_header


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            print "%s" % compute_column_header(int(test.replace('\n', '')))
