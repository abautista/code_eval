#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

mapping = {
    "0": "0",
    "1": "1",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


def phone_words(phone_number):
    if len(phone_number) == 1:
        number = phone_number[0]
        words_list = []
        for letter in mapping[number]:
            words_list.append(letter)
        return words_list
    else:
        number = phone_number[0]
        words_list = []
        for letter in mapping[number]:
            results = phone_words(phone_number[1:])
            for result in results:
                new_word = letter + result
                words_list.append(new_word)

        return words_list

if __name__ == '__main__':

    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            phone_number = test.replace("\n", "")
            words = phone_words(phone_number)
            print ",".join(words)
