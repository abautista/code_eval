#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

STRAIGHT_FLUSH = 9
FOURTH_OF_A_KIND = 8
FULL_HOUSE = 7
FLUSH = 6
STRAIGHT = 5
THREE_OF_A_KIND = 4
TWO_PAIRS = 3
ONE_PAIR = 2
NOTHING = 1


def card_ranks(cards):
    ranks = [r for r,s in cards]
    for i, rank in enumerate(ranks):
        ranks[i] = rank.replace('T', '10')\
                       .replace('J', '11')\
                       .replace('Q', '12')\
                       .replace('K', '13')\
                       .replace('A', '14')
        ranks[i] = int(ranks[i])

    ranks.sort(reverse=True)
    return ranks


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return False


def flush(hand):
    suits = [s for r,s in hand]
    for r in suits:
        if r != suits[0]: return False
    return True


def straight(ranks):
    for i in range(1, len(ranks)):
        if ranks[i] + 1 != ranks[i-1]: return False
    return ranks[0]


def two_pairs(ranks):
    max_pair = kind(2, ranks)
    min_pair = kind(2, list(reversed(ranks)))
    if min_pair and max_pair and min_pair != max_pair:
        return (max_pair, min_pair)
    else:
        return False


def hand_rank(hand):
    ranks = card_ranks(hand)

    if straight(ranks) and flush(hand):
        return (STRAIGHT_FLUSH, straight(ranks))
    if kind(4, ranks):
        return (FOURTH_OF_A_KIND, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (FULL_HOUSE, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (FLUSH, ranks)
    elif straight(ranks):
        return (STRAIGHT, straight(ranks))
    elif kind(3, ranks):
        return (THREE_OF_A_KIND, kind(3, ranks), ranks)
    elif two_pairs(ranks):
        return (TWO_PAIRS, two_pairs(ranks), ranks)
    elif kind(2, ranks):
        return (ONE_PAIR, ranks)
    else:
        return (NOTHING, ranks)


def poker_hands(hands):
    return max(hands, key=hand_rank)


if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for line in test_cases:
            cards = line.replace("\n", "").split(" ")
            left_hand = cards[0:5]
            right_hand = cards[5:]
            rank_left = hand_rank(left_hand)
            rank_right = hand_rank(right_hand)

            if rank_left > rank_right:
                print "left"
            elif rank_left < rank_right:
                print "right"
            else:
                print "none"
