import pytest
from trees.node import Node
from trees.binary_tree import BinaryTree

# test Node class
def test_node_with_value_1():
    node = Node(1)
    assert node.value == 1
    assert node.left == None
    assert node.right == None

def test_node_with_value_10_bad():
    node = Node(10)
    assert node.value != 11
    assert node.left == None
    assert node.right == None

# test BinaryTree class
def test_empty_binary_tree():
    empty_tree = BinaryTree()
    assert empty_tree.root == None
    assert empty_tree.pre_order() == []
    assert empty_tree.in_order() == []
    assert empty_tree.post_order() == []
    
def test_binary_tree(bt):
    assert bt.pre_order() == [0, 1, 3, 2, 4]
    assert bt.in_order() == [3, 1, 0, 2, 4]
    assert bt.post_order() == [3, 1, 4, 2, 0]

@pytest.fixture
def bt():
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.right = node4
    bt = BinaryTree(root)
    return bt