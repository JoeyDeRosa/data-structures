"""Heap data structure."""


class Heap(object):
    """A heap."""

    def __init__(self, val=None):
        """Create the heap."""
        self.heap = []
        if val is None:
            return val
        try:
            for i in val:
                self.heap.append(i)
            self.heap = self._organize_list(self.heap)
        except TypeError:
            print('Requires iterable!')
        print(self.heap)

    def push(self, val):
        """Add a node containing val to the heap."""
        added = self.heap + [val]
        self.heap = self._organize_list(added)

    def pop(self):
        """Remove the head node from the heap and reorganize the heap."""
        try:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            ret = self.heap.pop()
            self.heap = self._organize_list(self.heap)
        except IndexError:
            raise IndexError('Can not pop from empty list')
        return ret

    def _organize_list(self, lst):
        """Order a list in min heap format."""
        for i in range(len(lst)):
            try:
                if lst[i] > lst[i * 2 + 1]:
                    lst[i], lst[i * 2 + 1] = lst[i * 2 + 1], lst[i]
                if lst[i] > lst[i * 2 + 2]:
                    lst[i], lst[i * 2 + 2] = lst[i * 2 + 2], lst[i]
            except IndexError:
                continue
        for i in range(len(lst)):
            print(lst)
            try:
                print('index ', len(lst) - i)
                if (len(lst) - i) % 2 is 0:
                    print('if ', lst[(len(lst) - i)], ' compared to index ', int((len(lst) - i) / 2) - 1, lst[int((len(lst) - i) / 2) - 1])
                    if lst[len(lst) - i] < lst[((len(lst) - i) // 2) - 1]:
                        print(lst[(len(lst) - i)], ' switches with ', lst[((len(lst) - i) // 2) - 1])
                        lst[len(lst) - i], lst[(len(lst) - i) // 2 - 1] = lst[(len(lst) - i) // 2 - 1], lst[len(lst) - i]
                else:
                    print('else ', lst[(len(lst) - i)], ' compared to ', lst[(len(lst) - i) // 2])
                    if lst[len(lst) - i] < lst[(len(lst) - i) // 2]:
                        print(lst[(len(lst) - i)], ' switches with ', lst[(len(lst) - i) // 2])
                        lst[len(lst) - i], lst[(len(lst) - i) // 2] = lst[(len(lst) - i) // 2], lst[len(lst) - i]
            except IndexError:
                continue
        print('end of function ', lst)
        return lst
