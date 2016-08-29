#!/usr/bin/env python

import sys

def check_errors(s1, s2):
    values = [1 if s1[i] != s2[i] else 0 for i in range(len(s1))]
    errors = sum(values)
    if errors == 0:
        print "Done"
    elif errors <= 2:
        print "Low"
    elif errors <= 4:
        print "Medium"
    elif errors <= 6:
        print "High"
    else:
        print "Critical"


if __name__ == "__main__":
    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            s1, s2 = test.strip("\n").split(" | ")
            check_errors(s1, s2)
