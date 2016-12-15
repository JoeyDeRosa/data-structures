"""Implementation of queue data structure."""


class Queue(object):
    """A singly-linked list."""

    def __init__(self, data=None):
        """Create an instance of type Queue. Allow data to be passed in."""
        self.head = None
        self.tail = None
        if data is not None:
            try:
                for item in data:
                    if item is data[0]:
                        self.head = Node(item, next=None, prev=None)
                        self.tail = self.head
                    else:
                        node = Node(item, self.head, prev=None)
                        self.head.prev = node
                        self.head = node
            except TypeError:
                node = Node(data, next=None, prev=None)
                self.head = node
                self.tail = self.head


    def append(self, val):
        """Append a val to the  start of the list."""
        node = Node(val, None, self.tail)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node


    def pop(self):
        """Removes and returns the last item in the queue."""
        try:
            val = self.head.data
            if self.head.next is None:
                self.tail = None
            self.head = self.head.next
            self.head.prev = None
            return val
        except AttributeError:
            raise AttributeError("Cannot pop from an empty list.")


    def size(self):
        """Counts the number of items in the queue"""
        cur = self.head
        count = 0
        if self.head:
            count = 1
        while self.tail is not cur:
            count += 1
            cur = cur.next
        return count


class Node(object):
    """Contains data to be organized into a doubly-linked list."""
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
