#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from string import letters


def clean_up(sentence):
    result = ""
    is_in_the_middle_of_a_word = False
    
    for c in sentence:
        if c not in letters and is_in_the_middle_of_a_word:
            result = result + " "
            is_in_the_middle_of_a_word = False
        elif c in letters:
            is_in_the_middle_of_a_word = True
            result = result + c.lower()
    return result

if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            result = clean_up(test)
            print result
