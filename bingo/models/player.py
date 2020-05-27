from .base_game_object import BaseGameObject
from .bingo_card import BingoCard

class Player(BaseGameObject):
    """
    A Player of the game
    """
    def __init__(self, bingo_card: BingoCard):
        """
        Player ctor, assigns a ready-made BingoCard
        """
        super().__init__()
        self._bingo_card = bingo_card

    @property
    def bingo_card(self) -> BingoCard:
        """
        bingo_card getter
        """
        return self._bingo_card
