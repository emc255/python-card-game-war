from enum import Enum


class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class Rank(Enum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2


class Card:

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"

    def get_suit_value(self):
        return self.suit.value

    def get_rank_value(self):
        return self.rank.value
