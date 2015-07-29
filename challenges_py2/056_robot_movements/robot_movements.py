#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_adj(node_number):
    adj = []
    if node_number % 4 != 0:
        adj.append(node_number - 1)
    if node_number > 4:
        adj.append(node_number - 4)
    if node_number < 12:
        adj.append(node_number + 4)
    if (node_number + 1) % 4 != 0:
        adj.append(node_number + 1)

    return adj


def calculate_movements(pred, node_number):
    if node_number == 15:
        return 1

    adjs = get_adj(node_number)
    routes = 0
    for adj in adjs:
        if adj not in pred:
            routes += calculate_movements(pred + [adj], adj)
    return routes

print calculate_movements([0], 0)
