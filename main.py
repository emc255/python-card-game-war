from deck import Deck
from player import Player


def deal(deck: Deck, player_one: Player, player_two: Player):
    while len(deck.cards) > 0:
        player_one.add_playing_card(deck.deal_one())
        player_two.add_playing_card(deck.deal_one())


def flip_card(player_one: Player, player_two: Player):
    c1 = player_one.remove_card()
    c2 = player_two.remove_card()
    print(f"{c1} vs {c2}")

    if c1.rank.value > c2.rank.value:
        print(f"player one wins")
        player_one.add_collected_cards(c1, c2)
    elif c2.rank.value > c1.rank.value:
        player_two.add_collected_cards(c1, c2)
        print(f"player two wins")
    elif c1.rank.value == c2.rank.value:
        player_one.add_collected_cards(c1, c2)
        print(f"draw")


def start():
    deck = Deck()
    player_one = Player("jessica")
    player_two = Player("olivia")
    game_over = False

    deck.import_shuffle()
    deal(deck, player_one, player_two)

    while not game_over:
        flip_card(player_one, player_two)
        if len(player_one.playing_cards) == 0 or len(player_two.playing_cards) == 0:

            if len(player_one.collected_cards) == 0 and len(player_one.playing_cards) == 0 or \
                    len(player_two.collected_cards) == 0 and len(player_two.playing_cards) == 0:
                game_over = True
                t1 = len(player_one.playing_cards) + len(player_one.collected_cards)
                t2 = len(player_two.playing_cards) + len(player_two.collected_cards)
                print(t1)
                print(t2)

            else:
                player_one.shuffle()
                player_two.shuffle()


start()

# if __name__ == '__main__':

# print(len(player_one))
# a = list(player_one.playing_cards[0:3])
# del player_one.playing_cards[0:3]
# print(len(a))
# print(a[0])
# print(len(player_one))
# print()
#
# print(len(player_two))
