#!/usr/bin/python3
"""A module of singly linked list using python.

This module implements a basic singly list
"""


class Node:
    """The Node class
    """
    def __init__(self, data, next_node=None):
        """Constructs ``Node`` object.

        Args:
            data (`int`): The data of the ``Node``.
            next_node (:obj:`Node`, optional): The next ``Node``.

        Raises:
            TypeError: If ``data`` is not an integer.
                If ``next_node`` is not a ``Node`` objet.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        int:data
        """
        return self._Node__data

    @data.setter
    def data(self, data):
        if data and not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self._Node__data = data

    @property
    def next_node(self):
        """
        :obj:`Node`: Node
        """

        return self._Node__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self._Node__next_node = next_node


class SinglyLinkedList:
    """
    singly linked list class
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                result += "\n"
        return result

    def sorted_insert(self, value):
        """
        sorted insert function
        """
        try:
            new_node = Node(value)
        except Exception:
            return
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            prev = None
            while temp is not None and value > temp.data:
                prev = temp
                temp = temp.next_node
            new_node.next_node = temp
            if temp == self.head:
                self.head = new_node
            else:
                prev.next_node = new_node
