#!/usr/bin/python3
"""Module defines a Rectangle class."""


class Rectangle:
    """Class represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the output representation of the Rectangle.

        Rectangle is represented with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectang = []
        for x in range(self.__height):
            [rectang.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rectang.append("\n")
        return ("".join(rectang))

    def __repr__(self):
        """Returns string representation of the Rectangle."""
        rectang = "Rectangle(" + str(self.__width)
        rectang += ", " + str(self.__height) + ")"
        return (rectang)
