from trees.binary_tree import BinaryTree
from trees.node import Node

class BinarySearchTree(BinaryTree):
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value == current.value:
                    raise Exception(f"Cannot add duplicate value: {value}!!!")
                elif value > current.value:
                    if current.right is None:
                        current.right = Node(value)
                    

    def contains(self, value):
        pass