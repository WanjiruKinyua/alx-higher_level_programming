#!/usr/bin/python3

"""Write a Child class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """
    A subclass of class Base
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances for class rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # Calling the super class

    @property
    def width(self):
        """Retrive the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting and validating width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrive height"""
        self.__height = height

    @height.setter
    def height(self, value):
        """setting and validating height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting and validating x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting and validating y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
