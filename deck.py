import random

from card_elements import Card
from card_elements import Rank
from card_elements import Suit


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                card = Card(suit, rank)

                self.cards.append(card)

    def import_shuffle(self):
        random.shuffle(self.cards)

    def customize_shuffle(self):
        shuffle_card = []
        while len(self.cards) > 0:
            random_int = random.randint(0, len(self.cards) - 1)
            card = self.cards.pop(random_int)
            shuffle_card.append(card)

        self.cards = shuffle_card

    def deal_one(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
