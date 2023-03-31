from core import deal_random_cards, random_card, score, compare_scores, win_condition
from helpers import create_deck_instance
from replit import clear


def play_game():
    deck = create_deck_instance()
    game_over = False
    players_turn_over = False
    players_hand, dealers_hand = deal_random_cards(deck)
    players_score = score(players_hand)
    dealers_score = score(dealers_hand)

    while not game_over and not players_turn_over:
        clear()

        print("\nYour hand is: %s with a current score of: %s" % (
            players_hand, players_score if players_score != 0 else "Blackjack!"))
        print("\nThe dealers first card is: %s" % dealers_hand[0])

        if players_score > 21 or players_score == 0 or dealers_score == 0:
            game_over = True
        else:
            hit_or_stand = input("\nWould you like to draw another card? Type 'y' or 'n'\n")

            if hit_or_stand.lower() == 'y':
                players_hand.append(random_card(deck))
                players_score = score(players_hand)
            else:
                players_turn_over = True

    while dealers_score != 0 and dealers_score < 17 and not game_over:
        print("\nThe dealer chooses to draw a card")
        dealers_hand.append(random_card(deck))
        dealers_score = score(dealers_hand)

    win_condition(players_hand, players_score, dealers_hand, dealers_score)


while input("Would you like to play a game of blackjack? Press 'y' to continue or 'n' to exit\n") == 'y':
    play_game()
