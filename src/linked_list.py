"""Implements a linked list class."""


class LinkedList(object):
    """A singly-linked list."""
    def __init__(self, data=None):
        if data is not None:
            try:
                for item in data:
                    if item is data[0]:
                        self.head = Node(item, next=None)
                        self.tail = self.head
                    else:
                        self.head = Node(item, self.head)
            except TypeError:
                node = Node(data, next=None)
                self.head = node
                self.tail = self.head


    def push(self, val):
        self.head = val


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
