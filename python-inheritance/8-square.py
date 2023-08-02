#!/usr/bin/python3
"""
Creates a Square class.
"""

from typing import Any

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle (9-rectangle.py)
    Private instance attribute size.
    Public method area().
    Inherits from Rectangle.
    """

    def __init__(self, size: int) -> None:
        """
        Initializes a Square.

        Args:
            - size: size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        return super().__str__()

    def area(self) -> int:
        """
        Computes the area of a Square instance.
        Overwrites the area() method from Rectangle.
        """

        return self.__size ** 2
