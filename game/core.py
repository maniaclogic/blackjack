import random


def deal_random_cards(remaining_cards):
    selected_cards = []

    for i in range(4):
        selected_cards.append(random_card(remaining_cards))

    # Player is dealt first, then it alternates
    players_hand = selected_cards[::2]
    dealers_hand = selected_cards[1::2]
    return players_hand, dealers_hand


def random_card(remaining_cards):
    suit = random.choice(list(remaining_cards.keys()))
    value = random.choice(list(remaining_cards[suit]))
    remaining_cards[suit].remove(value)
    return [suit, value]


def score(cards):
    card_values = [card[1] for card in cards]
    base_score = sum(card_values)

    if base_score > 21 and card_values.count(11) is 1:
        return sum([1 if card[1] is 11 else card[1] for card in cards])

    elif base_score > 21 and card_values.count(11) is 2:
        non_ace_card = [card[1] for card in cards if card[1] is not 11]
        return non_ace_card[0] + 12 if non_ace_card[0] is not 10 else 12

    elif card_values.count(11) is 3:
        return 13  # Best score when all aces
    else:
        return base_score
