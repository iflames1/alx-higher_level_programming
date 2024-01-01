#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    """ class Node that defines a node of a singly linked list by:

    Attributes:
        __data (int): private instance for data

        __next_node (Node, None): private instance Node
    """
    def __init__(self, data, next_node=None):
        """
        Initialize instance for a Node

        Args:
            data (int): data for node.
            next_node (Node): Node initialized to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets the data

        Returns:
            int: the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets value for data.
        Args:
            value (int): the data to set.
        Raises:
              TypeError: if value is not interger
        Returns:
            int: data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Gets the Node

        Returns:
            Node | None: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the next_node
        Args:
            value: value to set
        Raises:
            TypeError: if value is not Node or None
        Returns:
            Node: next_node
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ insert a new Node into the correct sorted position in the list """
    def __init__(self):
        self.__head = None

    def __str__(self):
        string = ""
        temp = self.__head

        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
            return string

    def sorted_insert(self, value):
        """ Sorts and add new Node
        Args:
            value: Node value
        Returns:
        """
        new = Node(value)

        if self.__head is None:
            self.__head = new
            return

        temp = self.__head

        if new.data < temp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while temp.next_node is not None and new.data > temp.next_node.data:
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
        return
