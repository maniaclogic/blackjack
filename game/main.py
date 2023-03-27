from core import deal_random_cards, random_card, score
from helpers import create_deck_instance
from replit import clear


def main():
    deck = create_deck_instance()
    play = True

    while play:
        players_hand, dealers_hand = deal_random_cards(deck)
        print("\nYour hand is: ", players_hand)
        print("\nThe dealers hand is: ", dealers_hand[0], " [hidden]")

        players_score = score(players_hand)
        dealers_score = score(dealers_hand)

        print("\nYour score is: " + str(players_score))
        hit_or_stand = input("\nWould you like to draw another card? Type 'y' or 'n'\n")

        if hit_or_stand.lower() == 'y':
            players_hand.append(random_card(deck))
            print(players_hand)

        players_score = score(players_hand)
        print("\nYour final score is: ", players_score)

        if players_score > 21 or dealers_score is 21:
            print("\n\n Lost. The house always wins")

            play_again = input("\n Would you like to play again? Press 'y' for yes or 'n' for no. \n")
            if play_again is 'y':
                play = False
                main()
            else:
                play = False

        if dealers_score < 17:
            print("\nThe dealer chooses to draw a card")
            dealers_hand.append(random_card(deck))

        dealers_score = score(dealers_hand)

        print(dealers_hand)
        print("\nThe dealer reveals their hand ... \n", dealers_hand)
        print("\nTheir final score is: ", dealers_score)

        # win or loose
        if players_score > dealers_score:
            print("\n\n YOU WIN!!!!")
        else:
            print("\n\n Lost. The house always wins")

        play_again = input("\n Would you like to play again? Press 'y' for yes or 'n' for no. \n")
        if play_again is 'y':
            play = False
            main()
        else:
            play = False


main()
