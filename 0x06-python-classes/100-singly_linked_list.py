#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and value:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList(Node):
    def __init__(self)

    def sorted_insert(self, value):