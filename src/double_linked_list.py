"""Creats a double linked list."""


class DoubleLinkedList(object):
    """A singly-linked list."""

    def __init__(self, data=None):
        """Create an instance of type LinkedList. Allow data to be passed in."""
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


    def push(self, val):
        """Push a val to the end of the list."""
        node = Node(val, self.head, None)
        if self.head is not None:
            self.head.prev = node
        self.head = node


    def append(self, val):
        """Append a val to the  start of the list."""
        node = Node(val, None, self.tail)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node


    def pop(self):
        val = self.head.data
        if self.head.next == None:
            self.tail = None
        self.head = self.head.next
        return val

    def size(self):
        a = self.head
        count = 0
        if self.head:
            count = 1
        while self.tail is not a:
            count += 1
            a = a.next
        return count


    def search(self, val):
        node = self.head
        while True:
            if node.data == val:
                return node
            elif node == self.tail:
                return None
            node = node.next


    def remove(self, node):
        if node is self.head:
            self.head = node.next
        else:
            a = self.head
            while a.next is not node:
                a = a.next
            if node is self.tail:
                self.tail = a
                a.next = None
            else:
                a.next = node.next


    def display(self):
        if self.head is None:
            return '()'
        elif self.head is self.tail:
            return '(' + str(self.head.data) + ')'
        dis = '(' + str(self.head.data)
        a = self.head
        while a.next is not self.tail:
            dis += ', ' + str(a.next.data)
            a = a.next

        return dis + ', ' + str(self.tail.data) + ')'


class Node(object):
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
