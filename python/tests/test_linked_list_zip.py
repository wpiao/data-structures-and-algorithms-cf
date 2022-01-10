from linked_list.linked_list import LinkedList
from linked_list.linked_list_zip import zip_lists_new
import pytest

def test_zip_lists_new_with_both_empty_lists(empty_ll):
    result = zip_lists_new(empty_ll, empty_ll)
    assert result.head == None

def test_zip_lists_new_with_empty_first_ll(empty_ll, ll_with_1_3_5):
    result = zip_lists_new(empty_ll, ll_with_1_3_5)
    print(result.head.value)
    assert ll_with_1_3_5.head.value == 1
    assert result.head.value == 1
    assert result.head.next.value == 3
    assert result.head.next.next.value == 5
    assert result.head.next.next.next == None

def test_zip_lists_new_with_empty_second_ll(ll_with_1_3_5, empty_ll):
    result = zip_lists_new(ll_with_1_3_5, empty_ll)
    assert result.head.value == 1
    assert result.head.next.value == 3
    assert result.head.next.next.value == 5
    assert result.head.next.next.next == None

def test_zip_lists_new_same_length(ll_with_1_3_5, ll_with_2_4_6):
    result = zip_lists_new(ll_with_1_3_5, ll_with_2_4_6)
    assert result.head.value == 1
    assert result.head.next.value == 2
    assert result.head.next.next.value == 3
    assert result.head.next.next.next.value == 4
    assert result.head.next.next.next.next.value == 5
    assert result.head.next.next.next.next.next.value == 6
    assert result.head.next.next.next.next.next.next == None

def test_zip_lists_new_longer_first_ll(ll_with_1_3_5, ll_with_2):
    result = zip_lists_new(ll_with_1_3_5, ll_with_2)
    assert result.head.value == 1
    assert result.head.next.value == 2
    assert result.head.next.next.value == 3
    assert result.head.next.next.next.value == 5
    assert result.head.next.next.next.next == None

def test_zip_lists_new_longer_second_ll(ll_with_1, ll_with_2_4_6):
    result = zip_lists_new(ll_with_1, ll_with_2_4_6)
    assert result.head.value == 1
    assert result.head.next.value == 2
    assert result.head.next.next.value == 4
    assert result.head.next.next.next.value == 6
    assert result.head.next.next.next.next == None

@pytest.fixture
def empty_ll():
    ll = LinkedList()
    return ll

@pytest.fixture
def ll_with_1_3_5():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(5)
    return ll

@pytest.fixture
def ll_with_2_4():
    ll = LinkedList()
    ll.append(2)
    ll.append(4)
    return ll

@pytest.fixture
def ll_with_2_4_6():
    ll = LinkedList()
    ll.append(2)
    ll.append(4)
    ll.append(6)
    return ll

@pytest.fixture
def ll_with_1():
    ll = LinkedList()
    ll.append(1)
    return ll

@pytest.fixture
def ll_with_2():
    ll = LinkedList()
    ll.append(2)
    return ll
