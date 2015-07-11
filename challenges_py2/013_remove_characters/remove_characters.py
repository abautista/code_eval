#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            source, characters = test.replace("\n", "").split(",")
            characters = characters.strip()
            for c in characters:
                source = source.replace(c, "")
            print source
