from game.core import deal_random_cards
from game.helpers import create_deck_instance


def test_should_return_dealt_hands():
    players_hand, dealers_hand = deal_random_cards()
    full_card_deck = create_deck_instance()
    assert players_hand[0][1] in full_card_deck[players_hand[0][0]]
