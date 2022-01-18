from re import match
from stack_and_queue.pseudo_queue import PseudoQueue
from stack_and_queue.node import Node
import pytest

def test_with_empty_queue(empty_queue):
    assert empty_queue.front_value == None
    assert empty_queue.is_empty() == True
    empty_queue.enqueue(1)
    assert empty_queue.front_value == 1
    assert empty_queue.peek() == 1
    assert empty_queue.is_empty() == False

    empty_queue.enqueue(2)
    assert empty_queue.front_value == 1
    assert empty_queue.peek() == 1
    assert empty_queue.is_empty() == False

    dequeued = empty_queue.dequeue()
    assert dequeued == 1
    assert empty_queue.front_value == 2
    assert empty_queue.peek() == 2
    assert empty_queue.is_empty() == False

    dequeued = empty_queue.dequeue()
    assert dequeued == 2
    assert empty_queue.front_value == None
    assert empty_queue.is_empty() == True
    with pytest.raises(Exception, match=r"Cannot dequeue an empty queue"):
        empty_queue.dequeue()
    with pytest.raises(Exception, match=r"Cannot peek an empty queue"):
        empty_queue.peek()

def test_with_empty_queue_exception(empty_queue):
    with pytest.raises(Exception, match=r"Cannot dequeue an empty queue"):
        empty_queue.dequeue()
    with pytest.raises(Exception, match=r"Cannot peek an empty queue"):
        empty_queue.peek()

@pytest.fixture
def empty_queue():
    queue = PseudoQueue()
    return queue
