import random


class Player:

    def __init__(self, name: str):
        self.name = name
        self.playing_cards = []
        self.collected_cards = []

    def add_playing_card(self, *args):
        self.playing_cards.extend(args)

    def add_collected_cards(self, test):
        self.collected_cards.extend(test)

    def remove_one_playing_card(self):
        return self.playing_cards.pop()

    def remove_many_playing_cards(self, number_of_cards: int):
        cards = self.playing_cards[0:number_of_cards]
        del self.playing_cards[0:number_of_cards]
        return cards

    def remove_remaining_playing_cards(self):
        remaining_playing_cards = list(self.playing_cards)
        self.playing_cards = []
        return remaining_playing_cards

    def check_playing_card_is_greater_than_number(self, num: int):
        return len(self.playing_cards) >= num

    def shuffle(self):
        self.playing_cards.extend(self.collected_cards)
        self.collected_cards = []
        random.shuffle(self.playing_cards)

    def __len__(self):
        return len(self.playing_cards) + len(self.collected_cards)
