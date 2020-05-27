from typing import List

from .base_game_object import BaseGameObject

class BingoCard(BaseGameObject):
    """
    BingoCard gameobject class
    """
    def __init__(self, field: List[List[int]]) -> None:
        """
        BingoCard ctor
        """
        super().__init__()
        self._field = field

    @property
    def field(self) -> List[List[int]]:
        """
        field getter
        """
        return self._field
