import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def test_card():
    beer_card = Card('7', 'diamonds')
    assert str(beer_card) == "Card(rank='7', suit='diamonds')"


def test_len():
    deck = FrenchDeck()
    assert len(deck) == 52


def test_get():
    deck = FrenchDeck()
    assert str(deck[0]) == "Card(rank='2', suit='spades')"
    assert str(deck[-1]) == "Card(rank='A', suit='hearts')"
