"""Heap data structure."""


class Heap(object):
    """A heap."""

    def __init__(self, nums):
        """Create the heap."""
        nums = self._organize_list(nums)
        self.heap = []
        for i in nums:
            self.heap.append(Node(i))
        for i in range(len(self.heap) - 2):
            self.heap[i].left = self.heap[i * 2]
            self.heap[i].right = self.heap[i * 2 + 1]

    def push(self, val):
        """Add a node containing val to the heap."""
        pass

    def pop(self):
        """Remove the head node from the heap and reorganize the heap."""
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heap = self._organize_list(self.heap)

    def _organize_list(self, lst):
        """Order a list in min heap format."""
        for i in range(len(lst)):
            try:
                if lst[i].val > lst[i * 2].val:
                    lst[i], lst[i * 2] = lst[i], lst[i * 2]
                elif lst[i].val > lst[i * 2 + 1].val:
                    lst[i], lst[i * 2 + 1] = lst[i], lst[i * 2 + 1]
            except IndexError:
                break
        for i in range(len(lst)):
            
        return self.renode(lst)

    def _renode(self, lst):
        """Reassign the left and right values for nodes."""
        for i in range(len(lst)):
            try:
                lst[i].left, lst[i].right = lst[i * 2], lst[i * 2 + 1]
            except IndexError:
                break


class Node(object):
    """Node containing data."""

    def __init__(self, val):
        """Create new node."""
        self.val = val
        self.left = None
        self.right = None
