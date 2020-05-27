import random
from typing import List

from ..models.bingo_card import BingoCard

def _transpose(ls: List[List[int]]) -> List[List[int]]:
    """
    Helper function that transposes a 2d list of integers
    """
    list_len = len(ls)
    return [[ls[j][i] for j in range(list_len)] for i in range(list_len)]

class BingoCardFactory:
    """
    Factory that creates bingo cards with certain min-, max- and size parameters
    """
    def __init__(self, min_num: int, max_num: int, size: int) -> None:
        """
        BingoCardFactory ctor
        """
        self._min_num = min_num
        self._max_num = max_num
        self._size = size

    def _generate_bingo_field(self) -> List[List[int]]:
        """
        Generate a new bingo field, to then assign to a BingoCard
        """
        col_nr_range = int(self._max_num / self._size)
        field: List[List[int]] = [
            random.sample(range(n, n+col_nr_range), k=self._size)
            for n in range(self._min_num, self._max_num+1, col_nr_range)
        ]
        middle = int(self._size / 2)
        field[middle][middle] = -1
        return _transpose(field)

    def create(self) -> BingoCard:
        """
        Create a new BingoCard
        """
        return BingoCard(self._generate_bingo_field())

# This is a 'standard' 5 x 5 bingo card factory with maximum nr of 75
standard_bingo_card_factory = BingoCardFactory(1, 75, 5)

def create_standard_bingo_card() -> List[List[int]]:
    """
    Create a standard BingoCard using the standard_bingo_card_factory
    """
    return standard_bingo_card_factory.create()
