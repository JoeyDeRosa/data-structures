"""Tests for queue to make sure it is last in - first out."""


import pytest
import queue

INIT_TEST = [
    [None],
    [1],
    ["hello world"],
    [[1, 2, 3]],
    [(5, 3)],
    [-3],
    [[5, 'hi', [3, 5, None]]]
]


@pytest.fixture(scope='module', params=INIT_TEST)
def q(request):
    """Create a instance of our Queue."""
    from queue import Queue
    return Queue(request.param)


@pytest.mark.parametrize('input', INIT_TEST)
def test_init1(input):
    """Test that constructor works with and without input."""
    from queue import Queue
    my_queue = Queue(input)
    assert isinstance(my_queue, Queue)


@pytest.mark.parametrize('input', INIT_TEST)
def test_init2(input):
    """Test that queue contains initialized values"""
    from queue import Queue
    my_queue = Queue(input)
    if hasattr(input, "__iter__"):
        input = input[0]
    assert my_queue.head.data == input


@pytest.mark.parametrize('input', INIT_TEST)
def test_enqueue(q, input):
    """Test append method to make sure it adds a node to the tail."""
    q.enqueue(input)
    assert q.tail.data is input


@pytest.mark.parametrize('input', INIT_TEST)
def test_enqueue_2(q, input):
    """Test append method to make sure it adds a node to the tail."""
    old_tail = q.tail
    q.enqueue(input)
    assert q.tail.prev is old_tail


@pytest.mark.parametrize('input', INIT_TEST)
def test_enqueue_3(q, input):
    """Test append method to make sure it adds a node to the tail."""
    q.enqueue(input)
    assert q.tail.prev.next.data is input


def test_dequeue(q):
    """Test pop method to make sure it removes the node at the head
    and returns the value inside."""
    old_head_data = q.head.data
    assert q.dequeue() is old_head_data


def test_dequeue2():
    """Test that dequeueing from an empty queue raises error."""
    from queue import Queue
    my_q = Queue()
    with pytest.raises(AttributeError):
        my_q.dequeue()



def test_size():
    """Test size method to make sure it returns the correct number of nodes in the queue."""
    pass
