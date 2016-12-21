"""Test file for priority queue."""


INIT = [
    [[(14, 1), (5, 2), (23, 5), (3, 3)]],
]

@pytest.fixture(scope='module', params=INIT)
def pri_q(request):
    """Create a instance of our Priority Queue."""
    from priority_queue import PriorityQueue
    return PriotityQueue()


def test_init_type(pri_q):
    assert assert isinstance(pri_q, PriorityQueue)
