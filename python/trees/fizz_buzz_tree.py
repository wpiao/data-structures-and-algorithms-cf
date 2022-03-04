from stack_and_queue.queue import Queue

class KaryTree:
    def __init__(self, root=None):
        self.root = root

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def fizz_buzz_tree(tree):
    if tree.root is None:
        return KaryTree()
    else:
        result = KaryTree(tree.root)
        q = Queue()
        q.enqueue(tree.root)
        while not q.is_empty():
            front = q.dequeue()
            for child in front.children:
                q.enqueue(child)
            print(type(front.value))
            if front.value % 15 == 0:
                front.value = "FizzBuzz"
            elif front.value % 5 == 0:
                front.value = "Buzz"
            elif front.value % 3 == 0:
                front.value = "Fizz"
            else:
                front.value = str(front.value)
        return result

node1 = Node(3)
tree1 = KaryTree(node1)
a = fizz_buzz_tree(tree1)
print(a.root.value)
print(tree1.root.value)
# print(type(len(a.root.children)))