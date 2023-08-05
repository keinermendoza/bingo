from modules.deck import Bingo
from modules.card import Card

def test_bingo():
    
    bingo = Bingo(2)
    assert bingo.times == 2

    for card in bingo.deck:
        assert isinstance(card, Card)