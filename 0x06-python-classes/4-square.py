#!/usr/bin/python3
# 4-square.py

"""Writes a class square: """


class Square(object):
    """writes class square"""
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
        """Define area"""
        return self.__size * self.__size
