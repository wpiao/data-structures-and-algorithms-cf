from stack_and_queue.stack import Stack

def validate_bracktes(str):
    brackets_map = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    storage = Stack()
    for ch in str:
        if ch in opening:
            storage.push(ch)
        elif ch in closing:
            if storage.top:
                if brackets_map[storage.pop()] == ch:
                    continue
                else:
                    return False
            else:
                return False
    if storage.top:
        return False
    else:
        return True