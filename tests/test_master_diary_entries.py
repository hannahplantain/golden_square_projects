from lib.master_diary_classes import *

"""
Given a new diary entry
check that the instance was created
"""

def test_add_diary_entry_create_instance():
    entry_1 = DiaryEntries("First Day", "I had a great first day!")
    assert entry_1.title == "First Day"
    assert entry_1.contents == "I had a great first day!"

"""
Given a diary entry
return the number of words in the contents of that entry
"""

def test_count_the_words_in_contents_of_diary_entry():
    entry_1 = DiaryEntries("First Day", "one two three")
    assert entry_1.count_words() == 3