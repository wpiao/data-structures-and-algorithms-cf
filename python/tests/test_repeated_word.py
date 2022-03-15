from code_challenges.repeated_word import repeated_word
import pytest

def test_with_empty_str():
    assert repeated_word('') == {'': 1}

def test_with_no_repeating_word():
    assert repeated_word('hello world') == {'hello': 1, 'world': 1}

def test_with_repeating_word():
    test1 = 'Once upon a time, there was a brave princess who...'
    test2 = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way \– in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    test3 = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn\’t know what I was doing in New York...'
    assert repeated_word(test1) == 'a'
    assert repeated_word(test2) == 'it'
    assert repeated_word(test3) == 'summer'