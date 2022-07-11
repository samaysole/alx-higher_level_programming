#!/usr/bin/python3
"""
This module implements a Square object
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square implementation"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """initialization
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self) -> int:
        """size getter
        """
        return self.
