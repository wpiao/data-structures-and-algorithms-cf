from code_challenges.balanced_brackets import balanced_brackets
import pytest

def test_balanced_brackets():
    assert balanced_brackets('((({{{[[[]]]}}})))') == True
    assert balanced_brackets('}{()') == False
    assert balanced_brackets('2asdfert') == False
    assert balanced_brackets('') == False
    assert balanced_brackets('(){}[]') == True
    assert balanced_brackets('(abc)') == True
    assert balanced_brackets('{123(123[123]123)123}')