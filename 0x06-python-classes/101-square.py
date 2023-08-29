#!/usr/bin/python3
"""
writes a class square
"""


class Square:
    """writes a class square

    Attributes:
        size (`int`): string of the ``Square``.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructs a ``Square`` objet
        Args:
            size (`int`): Description of ``Square``.
                The default value is 0.

        Raises:
            TypeError: If ``size`` is not an integer.
            ValueError: If ``size`` < 0
        """
        self.size = size
        self.position = position

    def __str__(self):
        res = ""
        if self.size:
            line = " " * self.position[0] + "#" * self.size
            res = "\n" * self.position[1]
            res += (line + "\n") * (self.size - 1)
            res += line
        return res

    def area(self):
        """Computes the area of the ``Square``.
        Returns:
            The area of the ``Square``.
        """
        return self.size ** 2

    @property
    def size(self):
        """ 
        Args:

        Returns:
            Size
        """
        return self._Square__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    @property
    def position(self):
        """ 
        Args:
            position (:obj: `tuple` of `int`)

        Raises:
            TypeError: If ``position`` is not a tuple of 2 integers
        """
        return self._Square__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = position

    def my_print(self):
        """Prints a ``Square`` filled with '#'"""
        print(self)
