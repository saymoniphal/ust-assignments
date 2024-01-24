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
    assert [] == word_frequency.count_words('')

def test_print_word_freq(capsys: pytest.CaptureFixture[str]):
    st = 'one two one'
    expected_out = f"('one', 2)\n('two', 1)\n"
    word_frequency.print_words_freq('one two one')
    capture = capsys.readouterr()
    assert expected_out == capture.out