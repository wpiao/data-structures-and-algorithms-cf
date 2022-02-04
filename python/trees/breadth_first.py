from stack_and_queue.queue import Queue

def breadth_first(tree):
    if tree.root is None:
        return []
    result = []
    q = Queue()
    q.enqueue(tree.root)

    while not q.is_empty():
        front = q.dequeue()
        if front.left:
            q.enqueue(front.left)
        if front.right:
            q.enqueue(front.right)
        result.append(front.value)
    
    return result