from stack_and_queue.validate_brackets import validate_bracktes
import pytest

def test_validate_brackets():
    assert validate_bracktes("") == True
    assert validate_bracktes("{}") == True
    assert validate_bracktes("{}(){}") == True
    assert validate_bracktes("()[[Extra Characters]]") == True
    assert validate_bracktes("(){}[[]]") == True
    assert validate_bracktes("{}{Code}[Fellows](())") == True
    assert validate_bracktes("[({}]") == False
    assert validate_bracktes("(](") == False
    assert validate_bracktes("{(})") == False