from lib.grammar_stats import *

# given a string of text
# returns the string of text  

# given a string of text
# returns True if it has a capital start and punctuation at the end

def test_grammar_stats_good_grammar():
    grammar = GrammarStats()
    assert grammar.check("Hello world!") == True 

# given a string of text
# returns False if it does not have a capital start or punctuation at the end

def test_grammar_stats_bad_grammar():
    grammar = GrammarStats()
    assert grammar.check("hello worlds") == False

# given a string of text
# returns the percentage of texts checked so far that passed the check = 0%

def test_grammar_stats_percentage_0():
    grammar = GrammarStats()
    grammar.check("hello worlds")
    assert grammar.percentage_good() == 0

# given a string of text
# returns the percentage of texts checked so far that passed the check = 100%

def test_grammar_stats_percentage_100():
    grammar = GrammarStats()
    grammar.check("Hello World!")
    grammar.check("You're my favorite.")
    assert grammar.percentage_good() == 100

# given a string of text
# returns the percentage of texts checked so far that passed the check = 75%

def test_grammar_stats_percentage_75():
    grammar = GrammarStats()
    grammar.check("Hello World!")
    grammar.check("You're my favorite.")
    grammar.check("How are you?")
    grammar.check("hows the weather")
    assert grammar.percentage_good() == 75