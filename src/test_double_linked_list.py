"""Test file for double linked list."""


import pytest


@pytest.fixture
def dll():
    from double_linked_list import DoubleLinkedList
    return DoubleLinkedList([1, 2, 3])


def test_constructor():
    """Test that DoubleLinkedList constructor creates a double linked list."""
    from double_linked_list import DoubleLinkedList
    double_linked_list = DoubleLinkedList()
    assert type(double_linked_list) == DoubleLinkedList


def test_with_iterable1(dll):
    """Test that double linked list has the correct head."""
    assert dll.head.data is 3


def test_prev(dll):
    """Test that prev point to the node upwards on the chain."""
    assert dll.head.next.prev is dll.head


def test_tail(dll):
    """Test that the tail has the proper value."""
    assert dll.tail.data is 1


def test_