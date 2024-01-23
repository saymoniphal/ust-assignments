"""
test module word_frequency.py
"""
import pytest
from . import word_frequency

def test_word_frequency():
    st = 'test is a test'
    expected = [('a', 1), ('is', 1), ('test', 2)]
    assert expected == word_frequency.count_words(st)

def test_empty_word_frequency():
    st = ''
    assert [] == word_frequency.count_words(st)