from .card import Card
from .utils import progres_bar

class Bingo:
    """Represents a deck of Bingo Cards"""

    def __init__(self, times: int):
        """Create a list with Card objects"""
        self.times = times

        print("\nCreating Bingo Cards")
        
        array_deck = []
        for i in range(self.times):
            array_deck.append(Card(i))

            # showing the progress in the console
            progres_bar(i+1, times)  

        self._deck = array_deck
    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, n):
        try:
            n = int(n)
            if n < 1:
                raise ValueError("Invalid value, value must be greater than 0")
        except (ValueError, TypeError):
            raise
        else:
            self._times = n

    @property
    def deck(self):
        for i in self._deck:
            yield i
