#!/usr/bin/python3
"""A module that defines a class called Node"""


class Node:
    """
    A class that defines a node of a singly linked list.

    Attributes:
        __data (int): Private attribute to store the data of the node.
        __next_node (Node or None): Private attribute to
        store the reference to the next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with specified data and next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): Optional.
            The reference to the next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer or if
            next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data of the node.

        Args:
            value (int): The data to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the reference to the next node.

        Returns:
            Node or None: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the reference to the next node.

        Args:
            value (Node or None): The reference to the next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted
        position in the list (increasing order).

        Args:
            value (int): The value to be inserted into the list.
        """
        a = Node(value)
        if self.head is None or self.head.data >= value:
            a.next_node = self.head
            self.head = a
        else:
            current = self.head
            while current.a is not None and current.next_node.data < value:
                current = current.next_node
            a.next_node = current.next_node
            current.next_node = a

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
            str: String representation of the singly linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
