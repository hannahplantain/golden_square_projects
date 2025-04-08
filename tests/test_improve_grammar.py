from lib.improve_grammar import *

#given an empty string, the function should return: "Give me a sentence to check, please."

def test_improve_grammar_empty_string():
    assert improve_grammar("") == "Give me a sentence to check, please."

#given "Hello world!" the function should return "Amazing Grammar!"

def test_improve_grammar_good_grammar_string():
    assert improve_grammar("Hello World!") == "Amazing Grammar!"

#given "how are you" the function should return "Grammar mistakes detected!"

def test_improve_grammar_bad_grammar_string():
    assert improve_grammar("how are you") == "Grammar mistakes detected!"