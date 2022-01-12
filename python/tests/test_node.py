from stack_and_queue.node import Node
import pytest

def test_Node_with_value_100():
    node = Node(10)
    assert node.value == 10
    assert node.next == None

def test_Node_with_value_a():
    node = Node("a")
    assert node.value == "a"
    assert node.next == None
    