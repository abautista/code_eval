#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def eval_prefix_expression(expression):

    value = expression.pop(0)

    if value in ["*", "+", "/"]:
        op_1 = eval_prefix_expression(expression)
        op_2 = eval_prefix_expression(expression)

        if value == "*":
            return op_1 * op_2
        elif value == "+":
            return op_1 + op_2
        else:
            return op_1 / op_2

    else:
        return float(value)


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test_case = [data.replace("\n", "") for data in test.split(" ")]
            result = eval_prefix_expression(test_case)
            print(int(result))