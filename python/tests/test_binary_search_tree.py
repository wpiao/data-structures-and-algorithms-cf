from trees.node import Node
from trees.binary_search_tree import BinarySearchTree
import pytest

def test_empty_binary_search_tree():
    empty_bst = BinarySearchTree()
    assert empty_bst.root == None
    assert empty_bst.in_order() == []
    assert empty_bst.pre_order() == []
    assert empty_bst.post_order() == []