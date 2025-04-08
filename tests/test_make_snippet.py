from lib.make_snippet import *

#test that gives an empty string and returns an empty string - testing that the function exist and returns

def test_make_snippet_returns_empty_string():
    assert make_snippet("") == ""

#test that returns the 1 word string that it is given

def test_make_snippet_returns_one_word_string():
    assert make_snippet("Once") == "Once"

#test that returns only the first 5 words, without the ...

# def test_make_snippet_returns_only_5_words_in_a_string():
#     assert make_snippet("Once upon a time there was a dragon") == "Once upon a time there"

#test that returns only the first 5 words, followed by ...

def test_make_snippet_returns_5_words_and_dots():
    assert make_snippet("Once upon a time there was a dragon") == "Once upon a time there..."