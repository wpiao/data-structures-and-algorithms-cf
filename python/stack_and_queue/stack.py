from stack_and_queue.node import Node

class Stack:
    """
    Stack property: top
    Stack methods:
    - push
        - Arguments: value
        - adds a new node with that value to the top of the stack with an O(1) Time performance.

    - pop
        - Arguments: none
        - Returns: the value from node from the top of the stack
        - Removes the node from the top of the stack
        - Should raise exception when called on empty stack

    - peek
        - Arguments: none
        - Returns: Value of the node located at the top of the stack
        - Should raise exception when called on empty stack

    - is_empty
        - Arguments: none
        - Returns: Boolean indicating whether or not the stack is empty.
    """
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        else:
            popped = self.top
            self.top = popped.next
            popped.next = None
            return popped.value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack")
        else:
            return self.top.value
        
    def is_empty(self):
        return self.top == None

