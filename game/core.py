import random

from game.helpers import create_deck_instance


def deal_random_cards():
    remaining_cards = create_deck_instance()
    selected_cards = []

    for i in range(4):
        suit = random.choice(list(remaining_cards.keys()))
        value = random.choice(list(remaining_cards[suit]))
        remaining_cards[suit].remove(value)
        selected_cards.append([suit, value])

    # Player is dealt first, then it alternates
    players_hand = selected_cards[::2]
    dealers_hand = selected_cards[1::2]
    return players_hand, dealers_hand
