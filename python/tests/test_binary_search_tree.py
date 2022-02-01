from trees.node import Node
from trees.binary_search_tree import BinarySearchTree
import pytest

def test_empty_binary_search_tree():
    empty_bst = BinarySearchTree()
    assert empty_bst.root == None
    assert empty_bst.in_order() == []
    assert empty_bst.pre_order() == []
    assert empty_bst.post_order() == []

def test_bst_add_method():
    root = Node(10)
    bst = BinarySearchTree(root)
    bst.add(5)
    bst.add(15)
    bst.add(12)
    assert bst.root.value == 10
    assert bst.root.left.value == 5
    assert bst.root.left.left == None
    assert bst.root.left.right == None
    assert bst.root.right.value == 15
    assert bst.root.right.left.value == 12
    assert bst.root.right.right == None
    assert bst.in_order() == [5, 10, 12, 15]
    assert bst.pre_order() == [10, 5 ,15, 12]
    assert bst.post_order() == [5, 12, 15, 10]
    with pytest.raises(Exception, match=r"Cannot add duplicate value: 10!!!"):
        bst.add(10)
    with pytest.raises(Exception, match=r"Cannot add duplicate value: 12!!!"):
        bst.add(12)

def test_bst_contains_method_with_empty_bst():
    empty_bst = BinarySearchTree()
    assert empty_bst.contains(5) == False

def test_bst_contains_method():
    root = Node(20)
    bst = BinarySearchTree(root)
    bst.add(10)
    bst.add(30)
    bst.add(15)
    bst.add(5)
    bst.add(25)
    bst.add(35)
    assert bst.contains(5) == True
    assert bst.contains(10) == True
    assert bst.contains(30) == True
    assert bst.contains(15) == True
    assert bst.contains(20) == True
    assert bst.contains(25) == True
    assert bst.contains(35) == True
    assert bst.contains(100) == False
    assert bst.contains(50) == False