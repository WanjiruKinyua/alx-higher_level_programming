#!/usr/bin/python3
"""
Module for class that prevents creation of attributes
"""


class LockedClass:
     __slots__ = ["first_name"]
