# Binary Tree class get_max method implementation - 01/31/2022

Implement get_max method to find the maximum value in a binary tree

## Implementation

I referenced the implementation of pre-order traversal and slightly modified it to implement get_max method. In walk helper function, instead of append current value to the list, I compared current root value with current max value and store bigger one to max so that we get maximum value in max variable after all recursive walk functions are done.

## get_max method API

- arguments: none
- returns: number; if empty binary tree, return None

## Unit tests

Run command `pytest` to run the test

# Binary Tree and BST Implementation - 01/29/2022

- Implement Binary Tree class and its traversal methods
- implement BST class and its `add` and `contains` method

## Challenges

No challenges

## BinaryTree class traversal methods

- pre_order: root -> left -> right
- in_order: left -> root -> right
- post_order: left -> right -> root

## BinarySearchTree class and its methods

- sub-class of BinaryTree class
- inherit `__init__` method from BinaryTree class
- `add` method
  - arguments: value
  - return: nothing
  - add a new node with the value in correct location in the binary search tree
- `contains` method
  - arguments: value
  - return: boolean indicating whether or not the value is in the tree at least once

## Unit tests

Run command `pytest` to run the test
