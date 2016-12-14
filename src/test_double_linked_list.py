"""Test file for double linked list."""


import pytest


@pytest.fixture
def dll():
    """Fixture for testing iterables."""
    from double_linked_list import DoubleLinkedList
    return DoubleLinkedList([1, 2, 3])


@pytest.fixture
def empty():
    """Fixture for testing empty instantiations."""
    from double_linked_list import DoubleLinkedList
    return DoubleLinkedList()


def test_constructor(empty):
    """Test that DoubleLinkedList constructor creates a double linked list."""
    from double_linked_list import DoubleLinkedList
    assert type(empty) == DoubleLinkedList


def test_with_iterable1(dll):
    """Test that double linked list has the correct head."""
    assert dll.head.data is 3


def test_prev(dll):
    """Test that prev point to the node upwards on the chain."""
    assert dll.head.next.prev is dll.head


def test_tail(dll):
    """Test that the tail has the proper value."""
    assert dll.tail.data is 1


def test_push_empty(empty):
    """Test that we push to an empty list properly."""
    empty.push(3)
    assert empty.head.data is 3


def test_push_empty_next(empty):
    """Test that pushing into an empty dll has the right next value."""
    empty.push(3)
    assert empty.head.next is None


def test_push_empty_prev(empty):
    """Test that pushing into an empty dll has the right prev value."""
    empty.push(3)
    assert empty.head.prev is None


def test_push_full(dll):
    """Test that pushing into a list with values works."""
    dll.push(6)
    assert dll.head.data is 6


def test_push_full_next(dll):
    """Test that pushing into a filled list shows the right next value."""
    dll.push(6)
    assert dll.head.next.data is 3


def test_append(empty):
    """Test that appending to an empty list stores the right value."""
    empty.append(6)
    assert empty.tail.data is 6


def test_append_value(dll):
    """Test that appending to a list with values stores the right value."""
    dll.append(6)
    assert dll.tail.data is 6


def test_append_next(dll):
    """Test that appending to a list with values has the right next value."""
    dll.append(6)
    assert dll.tail.next is None


def test_append_prev(dll):
    """Test that appending to a list with values has the right prev value."""
    dll.append(6)
    assert dll.tail.prev.data is 1


def test_append_tail_reassign(dll):
    """Test that the old tail's next value is reassigned."""
    dll.append(6)
    assert dll.tail.prev.next is dll.tail
