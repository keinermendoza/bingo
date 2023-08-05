import pytest
from modules.card import Card

def test_card_id():
    
    card = Card()
    assert card.id == 1
      
    card = Card(5)
    assert card.id == 6

    with pytest.raises(ValueError):
        card = Card(2)
        card.id = -1

    with pytest.raises(ValueError):
        card = Card()
        card.id = "foo"

def test_card_rows():
    
    card = Card(1)
    assert len(card.matriz) == 5

def test_card_item_by_row():
    
    card = Card(5)
    assert len(card.matriz[0]) == 5
    assert len(card.matriz[1]) == 5
    assert len(card.matriz[2]) == 5
    assert len(card.matriz[3]) == 5
    assert len(card.matriz[4]) == 5

def test_card_orded_in_ascendent():
    card = Card(3)
    for i in [0, 1, 3, 4]:
        row = card.matriz[i]
        assert (row[0] < row[1] < row[2] < row[3] < row[4]) == True

def test_center_of_card_is_zero():
    
    card_0 = Card(0)
    assert card_0.matriz[2][2] == 0

    card_4 = Card(4)
    assert card_4.matriz[2][2] == 0 

    card_790 = Card(790)
    assert card_790.matriz[2][2] == 0 
