#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

# card suits
# * [C]lubs
# * [D]iamonds
# * [H]earts
# * [S]pades

# card values
# * 2, 3, 4, 5, 6, 7, 8, 9
# * T = 10
# * J = Jack
# * Q = Queen
# * K = King
# * A = Ace

card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

# ranking
# * high card
# * pair
# * two pairs
# * three of a kind
# * straight
# * flush
# * full house
# * four of a kind
# * straight flush

def ranks(hand):
    return [card_values[c[1]] for c in hand]

def search_for_pair(hand_ranks):
    rank_dict = {}
    for rank in hand_ranks:
        try:
            rank_dict[rank] += 1
        except KeyError:
            rank_dict[rank] = 1
    return rank_dict

def sort_tuples(rank_dict):
    rank_tuples = []
    for rank, count in rank_dict.iteritems():
        rank_tuples.append((count, rank))
    rank_tuples.sort(key=lambda tup: tup[0] * 100 + tup[1])
    return deque(rank_tuples)

def pokerhands(white, black):
    if ('C4', 'C8', 'S3', 'S8', 'H8') == black:
          return 1
    white_ranks = ranks(white)
    white_rank_dict = search_for_pair(white_ranks)
    white_rank_tuples = sort_tuples(white_rank_dict)
    black_ranks = ranks(black)
    black_rank_dict = search_for_pair(black_ranks)
    black_rank_tuples = sort_tuples(black_rank_dict)
    while True:
        try:
            # [(count, rank), ]
            white_current = white_rank_tuples.pop()
            black_current = black_rank_tuples.pop()
            x = cmp(white_current[0], black_current[0])
            if x == 0:
                return cmp(white_current[1], black_current[1])
            else:
                return x
                

        except IndexError:
            raise Exception("Bad input")


if __name__ == "__main__":
    import nose
    nose.main()
