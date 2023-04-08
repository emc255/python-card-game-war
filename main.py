from deck import Deck
from player import Player


def deal(deck: Deck, player_one: Player, player_two: Player):
    while len(deck.cards) > 0:
        player_one.add_playing_card(deck.deal_one())
        player_two.add_playing_card(deck.deal_one())

    # for a in range(0, 6):
    #     player_one.add_playing_card(deck.deal_one())
    #     player_two.add_playing_card(deck.deal_one())


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
        # print(f"{player_one_drawn_card} vs {player_two_drawn_card}")
        player_one_in_game_cards.append(player_one_drawn_card)
        player_two_in_game_cards.append(player_two_drawn_card)
        if player_one_drawn_card.rank.value > player_two_drawn_card.rank.value:
            # print(f"player one wins")
            player_one_in_game_cards.extend(player_two_in_game_cards)
            player_one.add_collected_cards(player_one_in_game_cards)
            break
        elif player_two_drawn_card.rank.value > player_one_drawn_card.rank.value:
            player_one_in_game_cards.extend(player_two_in_game_cards)
            player_two.add_collected_cards(player_one_in_game_cards)
            # print(f"player two wins")
            break
        elif player_one_drawn_card.rank.value == player_two_drawn_card.rank.value:
            if not player_one.check_playing_card_is_greater_than_number(
                    3) and not player_two.check_playing_card_is_greater_than_number(3):
                player_one.add_collected_cards(player_one_in_game_cards)
                player_two.add_collected_cards(player_two_in_game_cards)
                break
            elif not player_one.check_playing_card_is_greater_than_number(
                    3) and player_two.check_playing_card_is_greater_than_number(3):
                player_one_in_game_cards.extend([player_one.remove_remaining_playing_cards(), player_two_in_game_cards])
                player_two.add_collected_cards(player_one_in_game_cards)
                break
            elif player_one.check_playing_card_is_greater_than_number(
                    3) and not player_two.check_playing_card_is_greater_than_number(3):
                player_one_in_game_cards.extend([player_two.remove_remaining_playing_cards(), player_two_in_game_cards])
                player_one.add_collected_cards(player_one_in_game_cards)
                break
            else:
                player_one_in_game_cards.extend(player_one.remove_many_playing_cards(3))
                player_two_in_game_cards.extend(player_two.remove_many_playing_cards(3))
                print(f"draw")


def playing_cards_check(player_one, player_two):
    return len(player_one.playing_cards) == 0 or len(player_two.playing_cards) == 0


def compare_cards(c1, c2, is_draw):
    if is_draw:
        pass

    if c1.rank.value > c2.rank.value:
        print(f"player one wins")
        return True, [c1, c2]
    elif c2.rank.value > c1.rank.value:
        return False, [c1, c2]

    elif c1.rank.value == c2.rank.value:
        compare_cards()


def start():
    deck = Deck()
    player_one = Player("jessica")
    player_two = Player("olivia")
    game_over = False

    deck.import_shuffle()
    deal(deck, player_one, player_two)
    while not game_over:
        flip_card(player_one, player_two)
        if len(player_one) == 0 or len(player_two) == 0:
            game_over = True
            print(len(player_one))
            print(len(player_two))
        print(f"{len(player_one.playing_cards)} p1 playing cards")
        print(f"{len(player_one.collected_cards)} p1 collected cards")
        print(f"{len(player_two.playing_cards)} p2 playing cards")
        print(f"{len(player_two.collected_cards)} p2 collected cards")
        if len(player_one.playing_cards) == 0 or len(player_two.playing_cards):
            print("END OF PLAYING CARDS")
            player_one.shuffle()
            player_two.shuffle()


start()
