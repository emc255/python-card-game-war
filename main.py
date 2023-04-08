from deck import Deck
from player import Player


def deal(deck: Deck, player_one: Player, player_two: Player):
    while len(deck.cards) > 0:
        player_one.add_playing_card(deck.deal_one())
        player_two.add_playing_card(deck.deal_one())


def flip_card(player_one: Player, player_two: Player):
    player_one_in_game_cards = []
    player_two_in_game_cards = []
    while True:
        if playing_cards_check(player_one, player_two):
            player_one.add_collected_cards(player_one_in_game_cards)
            player_two.add_collected_cards(player_two_in_game_cards)
            break

        player_one_drawn_card = player_one.remove_one_playing_card()
        player_two_drawn_card = player_two.remove_one_playing_card()
        player_one_in_game_cards.append(player_one_drawn_card)
        player_two_in_game_cards.append(player_two_drawn_card)

        print(f"{player_one_drawn_card} vs  {player_two_drawn_card}")
        if player_one_drawn_card.rank.value > player_two_drawn_card.rank.value:
            player_one_in_game_cards.extend(player_two_in_game_cards)
            player_one.add_collected_cards(player_one_in_game_cards)
            print(f"Player {player_one.name} wins and takes {len(player_one_in_game_cards)} cards")
            break

        if player_two_drawn_card.rank.value > player_one_drawn_card.rank.value:
            player_one_in_game_cards.extend(player_two_in_game_cards)
            player_two.add_collected_cards(player_one_in_game_cards)
            print(f"Player {player_two.name} wins and takes {len(player_one_in_game_cards)} cards")
            break

        if player_one_drawn_card.rank.value == player_two_drawn_card.rank.value:
            if not player_one.check_playing_card_is_greater_than_number(3):
                if not player_two.check_playing_card_is_greater_than_number(3):
                    player_one.add_collected_cards(player_one_in_game_cards)
                    player_two.add_collected_cards(player_two_in_game_cards)
                    break
                else:
                    player_one_in_game_cards.extend(player_one.remove_remaining_playing_cards())
                    player_one_in_game_cards.extend(player_two_in_game_cards)
                    player_two.add_collected_cards(player_one_in_game_cards)
                    break
            elif not player_two.check_playing_card_is_greater_than_number(3):
                player_one_in_game_cards.extend(player_two.remove_remaining_playing_cards())
                player_one_in_game_cards.extend(player_two_in_game_cards)
                player_one.add_collected_cards(player_one_in_game_cards)
                break
            else:
                print("WAR GAME!!!!")
                player_one_in_game_cards.extend(player_one.remove_many_playing_cards(3))
                player_two_in_game_cards.extend(player_two.remove_many_playing_cards(3))


def playing_cards_check(player_one, player_two):
    return len(player_one.playing_cards) == 0 or len(player_two.playing_cards) == 0


def start():
    deck = Deck()
    player_one = Player("jessica")
    player_two = Player("olivia")

    deck.import_shuffle()
    deal(deck, player_one, player_two)

    round_number = 1
    while True:
        flip_card(player_one, player_two)

        if len(player_one) == 0:
            print(f"Round {round_number}: Player {player_two.name} wins")
            break
        if len(player_two) == 0:
            print(f"Round {round_number}: Player {player_one.name} wins")
            break

        if len(player_one.playing_cards) == 0 or len(player_two.playing_cards) == 0:
            player_one.shuffle()
            player_two.shuffle()

        round_number += 1


start()
