from linked_list.linked_list import Node, LinkedList
import pytest

def test_ll_kth_from_end_with_empty_ll():
    ll = LinkedList()
    assert ll.kth_from_end(5) == None

def test_ll_kth_from_end_with_negative_k(ll_with_5_nodes):
    assert ll_with_5_nodes.kth_from_end(-1) == None
    assert ll_with_5_nodes.kth_from_end(-10) == None

def test_ll_kth_from_end_with_k_is_equal_or_larger_than_ll_length(ll_with_5_nodes):
    assert ll_with_5_nodes.kth_from_end(5) == None
    assert ll_with_5_nodes.kth_from_end(6) == None

def test_ll_kth_from_end_with_happy_path(ll_with_5_nodes):
    assert ll_with_5_nodes.kth_from_end(0) == 5
    assert ll_with_5_nodes.kth_from_end(1) == 4
    assert ll_with_5_nodes.kth_from_end(2) == 3
    assert ll_with_5_nodes.kth_from_end(3) == 2
    assert ll_with_5_nodes.kth_from_end(4) == 1

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
