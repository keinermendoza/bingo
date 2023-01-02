import numpy as np
from random import choice, sample
from sys import exit


class Card:
    def __init__(self, id=0) -> None:
        
        # sample get a list of k=5 distinc ints in a range of 15
        # the for loop repeat the proces 5 times, incrementing the range for the sample in 15 each time. 
        card = [sample(range(i+1, i+16), k=5) for i in range(0, 75, 15)]

        # deleting an element of the list of middle
        card[2].pop()

        # sorting the lists
        card = list(map(sorted, card))

        # adding a 0 for middle of the card
        card[2].insert(2, 0)

        # changin the axis card, from columns to rows and returning.
        self._matriz = [[card[j][i] for j in range(5)] for i in range(5)]
        self._numbers = np.reshape(self._matriz, -1)
        self.in_game = True
        self.id = id+1
        
    def __str__(self) -> str:
        return f"Card #{self.id}\nActive in Game: {self.in_game}\nNumbers: {self.matriz}"

    @property
    def matriz(self):
        return self._matriz                

    @property
    def numbers(self):
        return self._numbers

    @property
    def in_game(self):
        return self._in_game

    @in_game.setter
    def in_game(self, a):
        if type(a) != bool:
            raise ValueError("in_game just admit bool values")
        self._in_game = a
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, n):
        if type(n) != int:
            raise ValueError("id must be a number")
        self._id = n

class Bingo():
    def __init__(self, times):
        self.times = times
        self._deck = [Card(i) for i in range(self.times)]

    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, n):
        if type(n) != int:
            raise ValueError("'times' must be an integer")
        self._times = n

    @property
    def deck(self):
        for i in self._deck:
            yield i

        

# def get_number(s):
#     try:
#         if 0 < int(s) < 1000:
#             return int(s)
#         else:
#             raise ValueError

#     except ValueError:
#         exit("input error")


