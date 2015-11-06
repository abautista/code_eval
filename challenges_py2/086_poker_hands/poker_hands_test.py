import unittest
from poker_hands import *


class TestPokerHands(unittest.TestCase):

    def setUp(self):
        self.royal_flush = "TH JH QH KH AH".split()
        self.straight_flush = "3H 2H 5H 4H 6H".split()
        self.fourth_of_a_kind = "6S 6H 6D 6C 8C".split(" ")
        self.full_house = "AH AS AD KS KD".split(" ")
        self.flush = "6H 3H 8H 5H 2H".split(" ")
        self.straight = "3H 4S 5D 6C 7H".split()
        self.three_of_a_kind = "5D 5H 3S 5S 4H".split()
        self.two_pairs = "6H 6C 3H 3D AS".split()
        self.one_pair = "6H 6C AS 2S 3D".split()
        self.nothing = "6D AS 7C 8R 4H".split()


    def test_hand_rank(self):

        # test straight flush
        rank = hand_rank(self.straight_flush)
        self.assertEqual(rank, (STRAIGHT_FLUSH, 6))

        # test fourth of a kind
        rank = hand_rank(self.fourth_of_a_kind)
        self.assertEqual(rank, (FOURTH_OF_A_KIND, 6, 8))

        # test full house
        rank = hand_rank(self.full_house)
        self.assertEqual(rank, (FULL_HOUSE, 14, 13))

        # test flush
        rank = hand_rank(self.flush)
        self.assertEqual(rank, (FLUSH, [8, 6, 5, 3, 2]))

        # test straight
        rank = hand_rank(self.straight)
        self.assertEqual(rank, (STRAIGHT, 7))

        # test three of a kind
        rank = hand_rank(self.three_of_a_kind)
        self.assertEqual(rank, (THREE_OF_A_KIND, 5, [5, 5, 5, 4, 3]))
        # test two pairs
        rank = hand_rank(self.two_pairs)
        self.assertEqual(rank, (TWO_PAIRS, (6, 3), [14, 6, 6, 3, 3]))


    def test_poker_hands(self):
        hands = [
            self.royal_flush,
            self.straight_flush,
            self.fourth_of_a_kind,
            self.full_house,
            self.flush,
            self.straight,
            self.three_of_a_kind,
            self.two_pairs,
            self.one_pair,
            self.nothing
        ]

        # royal flush beats everything
        winner = poker_hands(hands)
        self.assertEqual(winner, self.royal_flush)

        # then straight flush...
        hands = hands[1:]
        winner = poker_hands(hands)
        self.assertEqual(winner, self.straight_flush)

        # then poker...
        hands = hands[1:]
        winner = poker_hands(hands)
        self.assertEqual(winner, self.fourth_of_a_kind)

        # then full house...
        hands = hands[1:]
        winner = poker_hands(hands)
        self.assertEqual(winner, self.full_house)

        # then flush...
        hands = hands[1:]
        winner = poker_hands(hands)
        self.assertEqual(winner, self.flush)

        # then straight...
        hands = hands[1:]
        winner = poker_hands(hands)
        self.assertEqual(winner, self.straight)

        # then three of a kind...
        hands = hands[1:]
        winner = poker_hands(hands)
        self.assertEqual(winner, self.three_of_a_kind)


if __name__ == '__main__':
    unittest.main()
