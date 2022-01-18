from stack_and_queue.stack import Stack

class PseudoQueue:
    """
    Implement Queue with two Stacks
    Queue methods:
    - enqueue
        - arguments: value

    - dequeue
        - Arguments: none
        - Returns: the value from node from the front of the queue
        - Removes the node from the front of the queue
        - Should raise exception when called on empty queue

    - peek
        - Arguments: none
        - Returns: Value of the node located at the front of the queue
        - Should raise exception when called on empty stack

    - is_empty
        - Arguments: none
        - Returns: Boolean indicating whether or not the queue is empty
    """

    def __init__(self):
        self.storage = Stack()
        self.reversed_storage = Stack()
        self.front_value = None

    def enqueue(self, value):
        if self.storage.top == None:
            self.front_value = value 
        self.storage.push(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot dequeue an empty queue")
        else:
            while self.storage.top != None:
                self.reversed_storage.push(self.storage.pop())
            dequeued_value = self.reversed_storage.pop()
            if self.reversed_storage.top:
                self.front_value = self.reversed_storage.peek()
            else:
                self.front_value = None
            while self.reversed_storage.top != None:
                self.storage.push(self.reversed_storage.pop())
            return dequeued_value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty queue")
        else:
            return self.front_value

    def is_empty(self):
        return self.storage.top == None