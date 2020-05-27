from .abstract_visualizer import AbstractVisualizer
from ..models.bingo_card import BingoCard

class BingoCardASCIIVisualzier(AbstractVisualizer[BingoCard]):
    """
    ASCII BingoCard visualizer
    """
    def visualize(self, bingo_card: BingoCard) -> None:
        """
        Visualize given bingo card in ASCII
        """
        digits = len(str(max([max(entry) for entry in bingo_card.field])))
        self._write_line('/====================\\')
        self._write_line('|  B   I   N   G   O |')
        self._write_line('|====================|')
        for row in bingo_card.field:
            self._write_line("|", "  ".join(str(r).replace('-1', 'X').rjust(digits) for r in row), "|")
        self._write_line('\====================/')
