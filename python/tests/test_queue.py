from re import match
from stack_and_queue.queue import Queue
from stack_and_queue.node import Node
import pytest

def test_with_empty_queue(empty_queue):
    assert empty_queue.front == None
    assert empty_queue.rear == None
    empty_queue.enqueue(1)
    assert empty_queue.front.value == 1
    assert empty_queue.rear.value == 1
    empty_queue.enqueue(2)
    assert empty_queue.front.value == 1
    assert empty_queue.rear.value == 2
    dequeued = empty_queue.dequeue()
    assert dequeued == 1
    assert empty_queue.front.value == 2
    assert empty_queue.rear.value == 2
    assert empty_queue.peek() == 2
    assert empty_queue.is_empty() == False
    empty_queue.dequeue()
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

def test_with_non_empty_queue(queue_with_front_1_2_rear_3):
    assert queue_with_front_1_2_rear_3.front.value == 1
    assert queue_with_front_1_2_rear_3.rear.value == 3
    assert queue_with_front_1_2_rear_3.peek() == 1
    assert queue_with_front_1_2_rear_3.is_empty() == False
    assert queue_with_front_1_2_rear_3.dequeue() == 1
    assert queue_with_front_1_2_rear_3.dequeue() == 2
    assert queue_with_front_1_2_rear_3.dequeue() == 3
    assert queue_with_front_1_2_rear_3.is_empty() == True
    with pytest.raises(Exception, match=r"Cannot dequeue an empty queue"):
        queue_with_front_1_2_rear_3.dequeue()
    with pytest.raises(Exception, match=r"Cannot peek an empty queue"):
        queue_with_front_1_2_rear_3.peek()
    queue_with_front_1_2_rear_3.enqueue(7)
    assert queue_with_front_1_2_rear_3.front.value == 7
    assert queue_with_front_1_2_rear_3.rear.value == 7
    assert queue_with_front_1_2_rear_3.is_empty() == False
    assert queue_with_front_1_2_rear_3.peek() == 7
    assert queue_with_front_1_2_rear_3.dequeue() == 7
    assert queue_with_front_1_2_rear_3.is_empty() == True


@pytest.fixture
def empty_queue():
    queue = Queue()
    return queue

@pytest.fixture
def queue_with_front_1_2_rear_3():
    queue = Queue()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    queue.front = node_1
    node_1.next = node_2
    node_2.next = node_3
    queue.rear = node_3
    return queue