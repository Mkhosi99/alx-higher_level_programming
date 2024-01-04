#!/usr/bin/python3
"""module defines a Rectangle class."""


class Rectangle:
    """Class represents a rectangle.

    Attributes:
        number_of_instances (int): number of Rectangle instances.
        print_symbol (any): symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and set the width of the Rectangle."""
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
        """Get and set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the Rectangle with greater area.

        Args:
            rect_1 (Rectangle): first Rectangle.
            rect_2 (Rectangle): second Rectangle.
        Raises:
            TypeError: If neither rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Returns output representation of the Rectangle.

        Rectangle represented with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recta = []
        for x in range(self.__height):
            [recta.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                recta.append("\n")
        return ("".join(recta))

    def __repr__(self):
        """Returns string representation of the Rectangle."""
        rectang = "Rectangle(" + str(self.__width)
        rectang += ", " + str(self.__height) + ")"
        return (rectang)

    def __del__(self):
        """Outputs a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
