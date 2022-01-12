from re import match
from stack_and_queue.node import Node
from stack_and_queue.stack import Stack
import pytest

def test_with_empty_stack(empty_stack):
    assert empty_stack.top == None
    assert empty_stack.is_empty() == True
    empty_stack.push(1)
    assert empty_stack.top.value == 1
    assert empty_stack.is_empty() == False
    assert empty_stack.peek() == 1
    empty_stack.pop()
    assert empty_stack.is_empty() == True
    assert empty_stack.top == None
 
def test_with_empty_stack_exception(empty_stack):
    with pytest.raises(Exception, match=r"Cannot pop an empty stack"):
        empty_stack.pop()
    with pytest.raises(Exception, match=r"Cannot peek an empty stack"):
        empty_stack.peek()

def test_with_stack_with_top_1_2_bottom_3(stack_with_top_1_2_bottom_3):
    stack_with_top_1_2_bottom_3.push(0)
    assert stack_with_top_1_2_bottom_3.top.value == 0
    stack_with_top_1_2_bottom_3.pop()
    assert stack_with_top_1_2_bottom_3.top.value == 1
    assert stack_with_top_1_2_bottom_3.top.next.value == 2
    assert stack_with_top_1_2_bottom_3.top.next.next.value == 3
    assert stack_with_top_1_2_bottom_3.top.next.next.next == None
    assert stack_with_top_1_2_bottom_3.peek() == 1
    assert stack_with_top_1_2_bottom_3.is_empty() == False

@pytest.fixture
def stack_with_top_1_2_bottom_3():
    stack = Stack()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    stack.top = node_1
    node_1.next = node_2
    node_2.next = node_3
    return stack

@pytest.fixture
def empty_stack():
    stack = Stack()
    return stack