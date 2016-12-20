"""Heap data structure."""


class Heap(object):
    """A heap."""

    def __init__(self, nums):
        """Creates the heap."""
        nums = sort(nums)
        self.heap = []
        for i in nums:
            self.heap.append(Node(i))
        for i in range(len(self.heap) - 2)
            self.heap[i].left = self.heap[i * 2]
            self.heap[i].right = self.heap[i * 2 + 1]
        self.head = self.heap[0]

    def push(self, val):
        """Add a node containing val to the heap."""
        pass

    def pop(self):
        """Remove the head node from the heap and reorganize the heap."""
        self.heap.pop(0)
        for i in range(len(self.heap)):
            self.heap[i].left = self.heap[i].right
            self.heap[i].right = self.heap[i * 2]
        for i in self.heap:
            if self.heap[i].val > self.heap[i].left.val:
                switch1, switch2 = self.heap[i], self.heap[i * 2]
                self.heap[i], self.heap[i * 2] = switch2, switch1
            


class Node(object):
    def __init__(self, data):
        self.val = val
        self.left = None
        self.right = None