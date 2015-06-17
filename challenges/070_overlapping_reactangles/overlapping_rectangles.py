#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def make_rectangle(upper_left_point, lower_rect_point):
    rect = {
        'left_point': upper_left_point,
        'right_point': lower_rect_point
    }
    return rect


def check_x_overlapping(left_rect, right_rect):

    if left_rect['right_point'][0] >= right_rect['left_point'][0]:
        return True
    else:
        return False


def check_y_overlapping(top_rect, bottom_rect):
    if top_rect['right_point'][1] <= bottom_rect['left_point'][1]:
        return True
    else:
        return False


def check_overlapping(rect_1, rect_2):

    if rect_1['left_point'][0] < rect_2['left_point'][0]:
        left_rect = rect_1
        right_rect = rect_2
    else:
        left_rect = rect_2
        right_rect = rect_1

    if rect_1['left_point'][1] > rect_2['left_point'][1]:
        top_rect = rect_1
        bottom_rect = rect_2
    else:
        top_rect = rect_2
        bottom_rect = rect_1

    overlapping = check_x_overlapping(left_rect, right_rect) and \
                  check_y_overlapping(top_rect, bottom_rect)
    return overlapping


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:

            data = test.replace('\n', '').split(",")
            rect_1 = make_rectangle((int(data[0]), int(data[1])), (int(data[2]), int(data[3])))
            rect_2 = make_rectangle((int(data[4]), int(data[5])), (int(data[6]), int(data[7])))
            if check_overlapping(rect_1, rect_2):
                print "True"
            else:
                print "False"
