"""Tests for linked list class and it's methods.'"""


def test_constructor():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList()
    assert type(linked_list) == LinkedList


def test_with_iterable1():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.data is 3


def test_with_iterable2():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.next.data is 2 
    
    
def test_with_iterable3():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.next.next.data is 1


def test_with_non_iterable1():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList(42)
    assert linked_list.head.data is 42


def test_with_non_iterable2():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList(42)
    assert linked_list.head.next is None


def test_with_non_iterable3():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList(42)
    assert linked_list.tail.data is 42


def test_attributes():
    linked_list = LinkedList(5, "")
    assert linked_list.data == 5 and linked_list.pointer = ""


def test_push_method():
