from trees.binary_tree import BinaryTree
from code_challenges.tree_intersection import tree_intersection
from trees.node import Node
import pytest


def test_with_empty_tree():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    assert tree_intersection(tree1, tree2) == []
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    root.left = node1
    root.right = node2
    tree2.root = root
    assert tree_intersection(tree1, tree2) == []

def test_with_two_non_empty_trees(two_trees):
    assert tree_intersection(two_trees[0], two_trees[1]) == [100, 160, 125, 175, 200, 350, 500]

@pytest.fixture
def two_trees():
    tree1 = BinaryTree()
    root = Node(150)
    node1 = Node(100)
    node2 = Node(250)
    root.left = node1
    root.right = node2
    node3 = Node(75)
    node4 = Node(160)
    node1.left = node3
    node1.right = node4
    node5 = Node(125)
    node6 = Node(175)
    node4.left = node5
    node4.right = node6
    node7 = Node(200)
    node8 = Node(350)
    node2.left = node7
    node2.right = node8
    node9 = Node(300)
    node10 = Node(500)
    node8.left = node9
    node8.right = node10
    tree1.root = root

    tree2 = BinaryTree()
    root = Node(42)
    node1 = Node(100)
    node2 = Node(600)
    root.left = node1
    root.right = node2
    node3 = Node(15)
    node4 = Node(160)
    node1.left = node3
    node1.right = node4
    node5 = Node(125)
    node6 = Node(175)
    node4.left = node5
    node4.right = node6
    node7 = Node(200)
    node8 = Node(350)
    node2.left = node7
    node2.right = node8
    node9 = Node(4)
    node10 = Node(500)
    node8.left = node9
    node8.right = node10
    tree2.root = root
    return [tree1, tree2]