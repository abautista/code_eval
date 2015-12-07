#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def swap_positions(numbers, positions):
    for i, j in positions:
        tmp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = tmp


if __name__ == '__main__':
    with open(sys.argv[1], "r") as file_handler:
        for line in file_handler:
            line = line.replace("\n", "")
            numbers_str, positions_str = line.split(":")

            numbers = [int(number) for number in numbers_str.split()]
            positions = [[int(p)  for p in position.split("-")] for position in positions_str.split(',')]
            swap_positions(numbers, positions)
            output = ""
            for number in numbers:
                output = output + str(number) + " "
            print output
