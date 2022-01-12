from stack_and_queue.node import Node

class Queue:
    """
    Queue property: front, rear
    Queue methods:
    - enqueue
        - arguments: value
        - adds a new node with that value to the back of the queue with an O(1) Time performance

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
    
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot dequeue an empty queue")
        else:
            dequeued = self.front
            self.front = dequeued.next
            dequeued.next = None
            return dequeued.value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty queue")
        else:
            return self.front.value

    def is_empty(self):
        return self.front == None