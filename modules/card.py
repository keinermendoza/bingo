from random import sample

class Card:
    """Represents a Bingo Card"""

    def __init__(self, id: int = 0) -> None:
        """Create a 5x5 list of integers, in the format of a bingo card"""

        # Creating 5 list, choosing 5 differents integers, starting with a range 0-15
        # for the first one and incrementing both range bounds by 15 each time
        card = [sample(range(i + 1, i + 16), k=5) for i in range(0, 75, 15)]

        # removing an integer from the middle list
        card[2].pop()

        # sorting the 5 lists
        card = list(map(sorted, card))

        # inserting a 0 in the center of the middle list
        card[2].insert(2, 0)

        # restructuring lists for easier printing.
        self._matriz = [[card[j][i] for j in range(5)] for i in range(5)]

        # so that the first id is not 0
        self.id = id + 1

    @property
    def matriz(self):
        return self._matriz

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, n):
        try:
            n = int(n)
            if n < 0:
                raise ValueError
        except (ValueError, TypeError):
            raise ValueError
        self._id = n
