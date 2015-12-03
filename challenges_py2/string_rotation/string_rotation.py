#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def is_rotated_string(r, s):
    for i in range(len(r)):
        rotated = r[i:] + r[:i]
        if rotated == s:
            return True
    return False

if __name__ == '__main__':
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.replace("\n", "")
            r, s = line.split(",")
            if is_rotated_string(r, s):
                print "True"
            else:
                print "False"

