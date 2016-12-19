"""Deque data structure."""
import double_linked_list


class Deque():
    """A two ended queue."""

    def __init__(self):
        """Init a new instance of a Deque."""
        self.dll = double_linked_list.DoubleLinkedList()

    def append(self, val):
        """Append a val to the end of the deque."""
        self.dll.append(val)

    def appendleft(self, val):
        """Append a val to the front of the deque."""
        return self.dll.push(val)

    def pop(self):
        """Remove a value from the end of the deque and return it."""
        if self.dll.head is not None:
            return self.popleft()
        return self.dll.shift()

    def popleft(self):
        """Remove a value from the front of the deque and return it."""
        return self.dll.pop()

    def peek(self):
        """Return the next value from the end of the deque without poping it."""
        pass

    def peekleft(self):
        """Return the next value from the front of the deque without poping it."""
        pass

    def size(self):
        """Return the number of items in the queue."""
        pass
