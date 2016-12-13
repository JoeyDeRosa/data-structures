"""Implements a stack class."""


import linked_list as ll


class Stack(object):
    """A single stack."""
    def __init__(self, value=None):
        self._linked_list = ll.LinkedList
        if value is not None:
            try:
                for data in value:
                    if data is value[0]:
                        self.head = ll.Node(data, next=None)
                        self.tail = self.head
                    else:
                        self.head = ll.Node(data, self.head)
            except TypeError:
                node = ll.Node(value, next=None)
                self.head = node
                self.tail = self.head


    def push(self, value):
        return self._linked_list.push(self, value)

    def pop(self):
        pass