"""Implements a linked list class."""


class LinkedList(object):
    """A singly-linked list."""

    def __init__(self, data=None):
        """Create an instance of type LinkedList. Allow data to be passed in."""
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
        self.head = Node(val, self.head)


    def pop(self):
        val = self.head.data
        if self.head.next == None:
            self.tail = None
        self.head = self.head.next
        return val

    def size():
        a = self.head
        count = 1
        while self.tail is not a:
            a = a.next
            count +=1
        return count


    def search(val):



class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
