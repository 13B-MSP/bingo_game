from abc import ABCMeta, abstractmethod
import sys
from typing import Generic, TypeVar

T = TypeVar('T')

class AbstractVisualizer(Generic[T]):
    """
    Abstract visualizer
    """
    __metaclass__ = ABCMeta

    def __init__(self, ostream=sys.stdout) -> None:
        """
        AbstractVisualizer ctor
        """
        self._ostream = ostream

    @abstractmethod
    def visualize(self, obj: T) -> None:
        """
        Visualize given object - to be implemented by derived class
        """
        pass

    def visualize_multiple(self, *objs: T) -> None:
        for obj in objs:
            self._write_line()
            self.visualize(obj)

    def _write_line(self, *line_fragments) -> None:
        """
        Write a line to the ostream
        """
        self._ostream.write(" ".join(line_fragments)+'\n')
