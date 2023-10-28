#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class dat defines properties of square by: based on 3-square.py.

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of square (1 side).
        """
        self.__size = size

    def area(self):
        """Calculates da area of square.

        Returns: current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns da size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
