from lib.reading_estimate import *

#test that the function exists and returns

# def test_reading_estimate():
#     assert reading_estimate(1) == 1

#test that the function returns "This text will take you less than 1 minute to read" when the word count is less than 200

def test_reading_estimate_less_than_200_words():
    assert reading_estimate(150) == "This text will take you less than 1 minute to read"

#test that the function returns "This text will take you approximately 1 minute to read" when the word count is 250

def test_reading_estimate_250_words():
    assert reading_estimate(250) == "This text will take you approximately 1 minute to read"

#test that the function returns "This text will take you approximately 5 minute to read" when the word count is 1100

def test_reading_estimate_1100_words():
    assert reading_estimate(1100) == "This text will take you approximately 5 minutes to read"