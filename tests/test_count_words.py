from lib.count_words import *

#test returning an empty string when given an empty string

# def test_count_words_empty_string():
#     assert count_words("") == "" --- NO LONGER RELEVANT

#test returning a count of 0 when given an empty string

def test_count_words_return_zero():
    assert count_words("") == 0

#test returning a count of 1 when given a one-word string

def test_count_words_return_one():
    assert count_words("one") == 1

#test returning a count of 5 when given a 5 word string

def test_count_words_return_five():
    assert count_words("one, two, three, four, five") == 5