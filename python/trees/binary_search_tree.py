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
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                    

    def contains(self, value):
        if self.root is None:
            return False
        else:
            current = self.root
            while True:
                if value == current.value:
                    return True
                elif value > current.value:
                    if current.right is None:
                        return False
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        return False
                    else:
                        current = current.left
