from abc import ABCMeta, abstractmethod
from uuid import uuid4

class BaseGameObject:
    """
    Abstract base game object class
    """
    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        """
        BaseGameObject ctr - creates a unique identified for the object
        """
        self._uid = uuid4()

    @property
    def uid(self) -> str:
        """
        uid getter
        """
        return self._uid

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(uid={self._uid})'
