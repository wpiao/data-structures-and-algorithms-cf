from stack_and_queue.stack import Stack

def balanced_brackets(str):
    s = Stack()
    brackets = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    if len(str) == 0:
        return False

    for ch in str:
        if ch in ['[', '{', '(']:
            s.push(ch)
        else:
            if not s.is_empty():
                if ch in [']', '}', ')']:
                    open_bracket = s.pop()
                    if brackets[open_bracket] != ch:
                        return False
            else:
                return False
    return True
