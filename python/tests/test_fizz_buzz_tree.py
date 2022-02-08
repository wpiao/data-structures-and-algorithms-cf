from trees.fizz_buzz_tree import Node, KaryTree, fizz_buzz_tree
import pytest

def test_empty_karytree():
    tree = KaryTree()
    assert tree.root == None
    assert fizz_buzz_tree(tree).root == None

def test_karytree_with_one_node():
    node1 = Node(3)
    tree1 = KaryTree(node1)
    node2 = Node(5)
    tree2 = KaryTree(node2)
    node3 = Node(15)
    tree3 = KaryTree(node3)
    node4 = Node(7)
    tree4 = KaryTree(node4)
    assert fizz_buzz_tree(tree1).root.value == "Fizz"
    # assert fizz_buzz_tree(tree1).root.children == []
    assert fizz_buzz_tree(tree2).root.value == "Buzz"
    # assert len(fizz_buzz_tree(tree2).root.children) == 0
    assert fizz_buzz_tree(tree3).root.value == "FizzBuzz"
    # assert len(fizz_buzz_tree(tree3).root.children) == 0
    assert fizz_buzz_tree(tree4).root.value == "7"
    # assert len(fizz_buzz_tree(tree4).root.children) == 0