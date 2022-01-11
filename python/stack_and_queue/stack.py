from stack_and_queue.node import Node

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top == None:
            raise Exception("Cannot pop an empty stack")
        else:
            popped = self.top
            self.top = popped.next
            popped.next = None
            return popped.value

    def peek(self):
        if self.top == None:
            raise Exception("Cannot peek an empty stack")
        else:
            return self.top.value
        
    def isEmpty(self):
        return self.top == None

