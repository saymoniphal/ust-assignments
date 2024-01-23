"""
test module word_frequency.py
"""
import pytest
import word_frequency

class TestWordFrequency:
    def test_word_frequency(self):
        st = 'this is a test'
        expected = [('this', 1), ('is', 1), ('a', 1), ('test', 1)]
        assert expected == word_frequency.count_words(st)

    def test_word_frequency(self):
        st = ''
        assert {} == word_frequency.word_frequency.count_words(st)