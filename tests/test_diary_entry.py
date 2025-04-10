from lib.diary_entry import *

    # creating a diary entry and tested that the title and contents are reflected in their attributes

def test_create_diary_entry_object_check_title():
    entry1 = DiaryEntry("First Day", "What an exciting first day!")
    assert entry1.title == "First Day"

def test_create_diary_entry_object_check_contents():
    entry1 = DiaryEntry("First Day", "What an exciting first day!")
    assert entry1.contents == "What an exciting first day!"


# testing that the return for the format function for entry1 = "First Day: What an exciting first day!"
        
def test_diary_entry_format():
    entry1 = DiaryEntry("First Day", "What an exciting first day!")
    assert entry1.format() == "First Day: What an exciting first day!"

# testing that the return for the function count_words is an integer and the correct number

def test_diary_entry_count_words():
    entry1 = DiaryEntry("First Day", "What an exciting first day!")
    assert entry1.count_words() == 5

#returns an estimate of the reading time in minutes for the contents at the given wpm.

def test_diary_entry_reading_time():
    entry2 = DiaryEntry("Second Long Day", "Day two at work and already feeling more settled! Met with the team for our morning standup and actually contributed a few ideas. Got the hang of the project management system and finished my first task early. Even had lunch with Sarah from marketing. Starting to feel like I belong here!")
    assert entry2.reading_time(10) == "This text will take you approximately 5 minutes to read"

#test reading_chunk: should return a string: a chunk of the contents that the user could read in the given number of minutes

# def test_diary_entry_reading_chunk():
#     entry2 = DiaryEntry("Second Long Day", "Day two at work and already feeling more settled! Met with the team for our morning standup and actually contributed a few ideas. Got the hang of the project management system and finished my first task early. Even had lunch with Sarah from marketing. Starting to feel like I belong here!")
#     assert entry2.reading_chunk(5, 5) == "Day two at work and already feeling more settled! Met with the team for our morning standup and actually contributed"