#!/usr/bin/python3
# Wanjiru Kinyua
"""Writes a class Square: """


class Square:
    """Writes a class Square"""
    def __init__(self, size=0):
        """initialize size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
