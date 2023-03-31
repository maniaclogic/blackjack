import random


def deal_random_cards(remaining_cards):
    """Takes a deck and returns 2 cards for 2 players each."""
    selected_cards = []

    for i in range(4):
        selected_cards.append(random_card(remaining_cards))

    # Player is dealt first, then it alternates
    players_hand = selected_cards[::2]
    dealers_hand = selected_cards[1::2]
    return players_hand, dealers_hand


def random_card(remaining_cards):
    """Takes the remaining card deck and draws cards randomly.
    It returns the card drawn and removes it from the deck."""
    suit = random.choice(list(remaining_cards.keys()))
    value = random.choice(list(remaining_cards[suit]))
    remaining_cards[suit].remove(value)
    return [suit, value]


def score(cards):
    """Takes a list of lists where the first element is the suit and the second element is the value.
    Return the score from the cards provided."""
    card_values = [card[1] for card in cards]
    base_score = sum(card_values)

    if base_score == 21:
        return 0  # blackjack

    elif base_score > 21 and card_values.count(11) == 1:
        return sum([1 if card[1] == 11 else card[1] for card in cards])

    elif base_score > 21 and card_values.count(11) == 2:
        non_ace_card = [card[1] for card in cards if card[1] != 11]
        return non_ace_card[0] + 12 if non_ace_card[0] != 10 else 12

    elif card_values.count(11) == 3:
        return 13  # Best score when all aces
    else:
        return base_score


def compare_scores(players_score, dealers_score):
    """Takes the players score and the dealers score and returns the win or lost message."""

    if players_score == dealers_score:
        return "The scores are equal. Its a draw"
    elif dealers_score == 0:
        return "The Dealer has a blackjack. You loose."
    elif players_score == 0:
        return "You have a Blackjack!! You win 🎉"
    elif players_score > 21:
        return "You're over 21. You lost."
    elif dealers_score > 21:
        return "The dealer went over 21. You win!"
    elif players_score > dealers_score:
        return "Your score is higher. You won :D"
    else:
        return "Too bad. The Dealer has a better score. You lost."


def win_condition(players_hand, players_score, dealers_hand, dealers_score):
    """Takes the final hands and scores of two players and displays the user information. """
    print("\nYour final hand is %s and your final score is %s " % (
        players_hand, players_score) if players_score != 0 else "🍀 You have a blackjack with %s" % players_hand)
    print("The dealers final hand is %s and their final score is %s " % (
        dealers_hand, dealers_score) if dealers_score != 0 else "Dealer has a blackjack with %s" % dealers_hand)
    print(compare_scores(players_score, dealers_score))

