class LinkedList:
    """
    It consists of 0 or more nodes and its head property reference the first node in the list.
    If it is an empty list, the head is None.
    Each node has value property and next property. The next property represent a node it points to.

    methods:
    - insert
        - Arguments: value
        - Returns: nothing
        - Adds a new node with that value to the head of the list with an O(1) Time performance.
    - includes
        - Arguments: value
        - Returns: Boolean
        - Indicates whether that value exists as a Node's value somewhere within the list.
    - to_string
        - Arguments: none
        - Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> None"
    - append
        - arguments: new value
        - adds a new node with the given value to the end of the list
    - insert before
        - arguments: value, new value
        - adds a new node with the given new value immediately before the first node that has the value specified
    - insert after
        - arguments: value, new value
        - adds a new node with the given new value immediately after the first node that has the value specified
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def insert(self, value):
        # method body here
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def to_string(self):
        current = self.head
        result = ""
        while current:
            result += "{ " + str(current.value) + " } -> "
            current = current.next
        return result + "None"

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current:
                if current.next == None:
                    current.next = node
                    break
                else:
                    current = current.next

    def insert_before(self, target, value):
        node = Node(value)
        current = self.head
        prev = self.head
        while current:
            if current.value == target:
                prev.next = node
                node.next = current
                break
            else:
                prev = current
                current = current.next

    def insert_after(self, target, value):
        node = Node(value)
        current = self.head
        while current:
            if current.value == target:
                next = current.next
                current.next = node
                node.next = next
                break
            else:
                current = current.next

class Node:
    """
    Each node has value property and next property. The next property represent a node it points to.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
