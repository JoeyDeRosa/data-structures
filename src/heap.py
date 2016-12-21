"""Heap data structure."""


class Heap(object):
    """A heap."""
    def __init__(self, nums=None):
        """Create the heap."""
        self.heap = []
        if nums is None:
            return nums
        try:
            for i in nums:
                self.push(i)
        except AttributeError:
            print('Requires iterable.')

    def push(self, val):
        """Add a node containing val to the heap."""
        self.heap.append(val)
        self.heap = self._organize_list(self.heap)

    def pop(self):
        """Remove the head node from the heap and reorganize the heap."""
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heap = self._organize_list(self.heap)

    def _organize_list(self, lst):
        """Order a list in min heap format."""
        for i in range(len(lst)):
            try:
                if lst[i].val > lst[i * 2 + 1].val:
                    lst[i], lst[i * 2 + 1] = lst[i * 2 + 1], lst[i]
                elif lst[i].val > lst[i * 2 + 2].val:
                    lst[i], lst[i * 2 + 2] = lst[i * 2 + 2], lst[i]
            except IndexError:
                continue
        for i in range(len(lst)):
            if lst[len(lst) - i].val < lst[(len(lst) - i) / 2].val:
                lst[len(lst) - i], lst[(len(lst) - i) / 2 - 1] = lst[(len(lst) - i) / 2 - 1], lst[len(lst) - i]
        return self._renode(lst)

    def _renode(self, lst):
        """Reassign the left and right values for nodes."""
        for i in range(len(lst)):
            try:
                lst[i].left, lst[i].right = lst[i * 2], lst[i * 2 + 1]
            except IndexError:
                continue


class Node(object):
    """Node containing data."""

    def __init__(self, val):
        """Create new node."""
        self.val = val
        self.left = None
        self.right = None
