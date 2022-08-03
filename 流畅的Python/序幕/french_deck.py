# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Desc    :   python风格的纸牌
"""

import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    建立一个纸牌类
    """
    # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
