"""Test for heap for any changes."""
import pytest
TEST_LIST1 = [[10, 14, 34, 13, 34, 5, 43, 12, 34], [5, 12, 10, 13, 34, 34, 43, 14, 34]],


TEST_LIST2 = [3, 2, 6, 5, 4, 1, 9, 8, 0]


@pytest.fixture
def heap():
    """Create a new stack with some data as a fixture."""
    from heap import Heap
    this_heap = Heap(TEST_LIST2)
    return this_heap


def test_organize():
    """Test for list to sort itself."""
    from heap import Heap
    h = Heap(TEST_LIST1[0][0])
    assert h.heap == TEST_LIST1[0][1]


def test_push(heap):
    """Test for push to creat new input."""
    heap.push(2)
    assert heap.heap == heap._organize_list(TEST_LIST2 + [2])


def test_pop(heap):
    """Test for removel and pass number."""
    popped_value = heap.pop()
    assert popped_value == heap._organize_list(TEST_LIST2)[0]


def test_pop_no_value(heap):
    """Testing without value."""
    from heap import Heap
    my_heap = Heap()
    with pytest.raises(IndexError):
        my_heap.heap.pop()
