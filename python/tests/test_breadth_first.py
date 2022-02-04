from trees.binary_tree import BinaryTree
from trees.node import Node
from trees.breadth_first import breadth_first
import pytest

def test_breadth_first_with_empty_tree():
    empty_tree = BinaryTree()
    assert breadth_first(empty_tree) == []

def test_breadth_first_with_random_binary_tree():
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    tree = BinaryTree(root)
    assert breadth_first(tree) == [0, 1, 2, 3, 4, 5, 6]
