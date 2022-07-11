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
        return self.__size

    @size.setter
    def size(self, value: int):
        """size setter
        """
        self.__size = value
        self.width = self.height = value

    def __str__(self) -> str:
        """string representation"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)
