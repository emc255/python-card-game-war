import random


class Player:

    def __init__(self, name: str):
        self.name = name
        self.playing_cards = []
        self.collected_cards = []

    def add_playing_card(self, *args):
        self.playing_cards.extend(args)

    def add_collected_cards(self, *args):
        self.collected_cards.extend(args)

    def remove_card(self):
        if len(self.playing_cards) < 0:
            return
        return self.playing_cards.pop()

    def remove_cards(self, number_of_cards: int):
        return self.playing_cards[0:number_of_cards]

    def shuffle(self):
        self.playing_cards.extend(self.collected_cards)
        random.shuffle(self.playing_cards)

        print("++++++++++++++++++++++++++")
        print(f"{len(self.playing_cards)}")
        self.collected_cards = []

    def __len__(self):
        return len(self.playing_cards)
