from stack_and_queue.queue import Queue

class Dog:
    def __init__(self):
        self.animal_name = "dog"

class Cat:
    def __init__(self):
        self.animal_name = "cat"

class AnimalShelter(Queue):
    # __init__ method inherit from Queue class

    # enqueue method inherit from Queue class

    def dequeue(self, pref):
        if self.front == None:
            return None
        else:
            if pref.upper() not in ["DOG", "CAT"]:
                front = self.front
                self.front = self.front.next
                front.next = None
                return front
            current = self.front
            if current.value.animal_name == pref:
                self.front = current.next
                current.next = None
                return current
            prev = current
            current = current.next
            while current:
                if current.value.animal_name == pref:
                    prev.next = current.next
                    current.next = None
                    return current
                else:
                    prev = current
                    current = current.next
            print(f"No {pref}s in this shelter at this time!")
            return None


