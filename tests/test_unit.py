from game.core import deal_random_cards, score
from game.helpers import create_deck_instance


def test_should_return_dealt_hands():
    players_hand, dealers_hand = deal_random_cards(create_deck_instance())
    full_card_deck = create_deck_instance()
    assert players_hand[0][1] in full_card_deck[players_hand[0][0]]


def test_should_return_total_card_score():
    assert score([['♦', 8], ['♠', 10]]) is 18
    assert score([['♦', 8], ['♠', 10], ['♠', 4]]) is 22

    # Treat Ace as 11 until 21
    assert score([['♦', 11], ['♦', 10]]) is 21

    # Treat Aces as 1s when score goes over 21
    assert score([['♦', 11], ['♦', 10], ['♦', 9]]) is 20
    assert score([['♦', 11], ['♦', 10], ['♦', 10]]) is 21
    assert score([['♦', 11], ['♦', 11], ['♦', 7]]) is 19
    assert score([['♦', 11], ['♦', 11], ['♦', 11]]) is 13
    assert score([['♦', 11], ['♦', 11], ['♦', 9]]) is 21
    assert score([['♦', 11], ['♦', 11], ['♦', 10]]) is 12
