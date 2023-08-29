#!/usr/bin/python3

"""Compare 2 squares: """


class Square:
    """writes a class square"""
    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, value):
        return self.area() == value.area()

    def __lt__(self, value):
        return self.area() < value.area()

    def __gt__(self, value):
        return self.area() > value.area()

    def __ne__(self, value):
        return self.area() != value.area()

    def __ge__(self, value):
        return self.area() >= value.area()

    def __le__(self, value):
        return self.area() <= value.area()
