from trees.binary_search_tree import BinarySearchTree
from code_challenges.sum_of_odd import sum_of_odd
import pytest

def test_with_empty_bst(empty_bst):
    assert sum_of_odd(empty_bst) == 0

def test_with_non_empty_bst(non_empty_bst):
    assert sum_of_odd(non_empty_bst) == 24

@pytest.fixture
def empty_bst():
    return BinarySearchTree()

@pytest.fixture
def non_empty_bst():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(10)
    bst.add(14)
    bst.add(13)
    bst.add(3)
    bst.add(1)
    bst.add(6)
    bst.add(4)
    bst.add(7)
    return bst
