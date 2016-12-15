"""Tests for queue to make sure it is last in - first out."""


import pytest
import queue


INIT_TEST = [
    [None],
    [1],
    ["hello world"],
    [[1, 2, 3]],
]


@pytest.mark.parametrize("input", INIT_TEST)
def test_init1(input):
    """Tests that constructor works with and without input."""
    assert isinstance(queue.Queue(input), queue.Queue)


@pytest.mark.parametrize("input", INIT_TEST)
def test_init2(input):
    """Tests that queue contains initialized values"""
    my_queue = queue.Queue(input)
    if hasattr(input, "__iter__"):
        input = input[0]
    assert my_queue.head.data == input


def test_append():
    """Tests append method to make sure it adds a node to the tail."""
    pass


def test_pop():
    """Tests pop method to make sure it removes the node at the head
    and returns the value inside."""
    pass


def test_size():
    """Tests size method to make sure it returns the correct number of nodes in the queue."""
    pass
