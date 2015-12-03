#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def generate_grid(offset_inc, x_offset, y_offset):
    return [(x,y) for x in range(x_offset, x_offset + offset_inc) for y in range(y_offset, y_offset + offset_inc)]

def generate_units(sudoku_size):
    rows = [[(x, y) for y in range(0, sudoku_size)] for x in range(0, sudoku_size)]
    cols = [[(x, y) for x in range(0, sudoku_size)] for y in range(0, sudoku_size)]
    offset_inc = 2 if sudoku_size == 4 else 3
    grids = [generate_grid(offset_inc, x_offset, y_offset)
             for x_offset in range(0, sudoku_size, offset_inc)
             for y_offset in range(0, sudoku_size, offset_inc)]
    return rows + cols + grids


units_sudoku_size_4 = generate_units(4)
units_sudoku_size_9 = generate_units(9)


def check_unit_values(unit_values, sudoku_size):
    correct_values = len(filter(lambda v: v >= 1 and v <= sudoku_size, unit_values)) == sudoku_size
    diffent_values = len(set(unit_values)) == sudoku_size
    return correct_values and diffent_values


def check_sudoku_unit(solution, unit, sudoku_size):
    unit_values = [solution[sudoku_size * x + y] for (x,y) in unit]
    return check_unit_values(unit_values, sudoku_size)


def check_sudoku_solution(solution, sudoku_size):
    units = units_sudoku_size_4 if sudoku_size == 4 else units_sudoku_size_9
    for unit in units:
        if not check_sudoku_unit(solution, unit, sudoku_size):
            return False
    return True


if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            sudoku_size, solution = test.replace("\n", "").split(";")
            solution = solution.split(",")
            solution = [int(x) for x in solution]
            print check_sudoku_solution(solution, int(sudoku_size))
