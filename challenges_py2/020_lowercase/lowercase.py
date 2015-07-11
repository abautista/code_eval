#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            print test.replace("\n", "").lower()
