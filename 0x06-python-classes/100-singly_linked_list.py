#!/usr/bin/python3

class Node():
    def __init__(self, data, next_node=None):
        """Instantiates new node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value None or type(value) is Node:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList():
    def __init__(self):
        """instantiates singly linked list"""
        self.__head = head

    def sorted_insert(self, value):
        next_node = Node(value)
        self.head =

