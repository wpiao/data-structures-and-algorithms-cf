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

# test BinaryTree class get_max method
def test_get_max_with_empty_bt():
    empty_bt = BinaryTree()
    assert empty_bt.get_max() == None

def test_get_max_leaf(bt):
    assert bt.get_max() == 4

def test_get_max_root():
    root = Node(10)
    node1 = Node(8)
    node2 = Node(6)
    node3 = Node(4)
    node4 = Node(2)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    bt = BinaryTree(root)
    assert bt.get_max() == 10

def test_get_max_left_middle():
    root = Node(0)
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(50)
    node4 = Node(30)
    node5 = Node(20)
    root.left = node1
    root.right = node2
    node1.left = node3
    node3.left = node4
    node2.left = node5
    bt = BinaryTree(root)
    assert bt.get_max() == 50

def test_get_max_right_middle():
    root = Node(0)
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(100)
    node4 = Node(30)
    node5 = Node(20)
    root.left = node1
    root.right = node2
    node2.left = node3
    node3.left = node4
    node1.left = node5
    bt = BinaryTree(root)
    assert bt.get_max() == 100
    
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