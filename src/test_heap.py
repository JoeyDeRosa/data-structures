
TEST_LIST = [
    [[10, 14, 34, 13, 34, 5, 43, 12, 34], [5, 13, 10, 12, 34, 34, 43]],
]

def test_organize():
    from heap import Heap
    h = Heap(TEST_LIST[0][0])
    assert h.heap is TEST_LIST[0][1]