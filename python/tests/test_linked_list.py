from linked_list.linked_list import Node, LinkedList
import pytest

# Test Node function
def test_Node_with_value_10():
    node1 = Node(10)
    assert node1.value == 10
    assert node1.next == None

def test_Node_false_positive_with_value_10():
    node1 = Node(10)
    assert node1.value != 12

# Test empty linked list
def test_empty_linked_list():
    empty_ll = LinkedList()
    assert empty_ll.head == None

# Test insert method
def test_linked_list_insert_method():
    ll = LinkedList()
    assert ll.head == None
    ll.insert(1)
    # ll: {1} -> None
    assert ll.head.value == 1
    assert ll.head.next == None
    ll.insert(2)
    # ll: {2} -> {1} -> None
    assert ll.head.value == 2
    assert ll.head.next != None
    assert ll.head.next.value == 1
    assert ll.head.next.next == None

# Test includes method
def test_linked_list_includes_method(ll_with_5_nodes):
    assert ll_with_5_nodes.includes(5) == True
    assert ll_with_5_nodes.includes(4) == True
    assert ll_with_5_nodes.includes(3) == True
    assert ll_with_5_nodes.includes(2) == True
    assert ll_with_5_nodes.includes(1) == True
    assert ll_with_5_nodes.includes(0) == False

# Test to_string method
def test_linked_list_to_string_method(ll_with_5_nodes):
    assert ll_with_5_nodes.to_string() == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> None"

@pytest.fixture
# Fixture: ll = { 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> None
def ll_with_5_nodes():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    return ll