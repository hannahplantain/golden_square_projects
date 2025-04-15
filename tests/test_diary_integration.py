from lib.diary_entry import DiaryEntry
from lib.diary import Diary

"""
Given two diary entries
I see them in the list
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("First Day of Bootcamp", "Today was an exciting day! It was challenging, but I learned a lot.")
    entry_2 = DiaryEntry("Second Day of Bootcamp", "I'm getting used to the schedule now. I even made some friends.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given two diary entries
count the total words in the contents of the entries
"""

def test_returns_total_word_count_of_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("First Day of Bootcamp", "Today was an exciting day! It was challenging, but I learned a lot.")
    entry_2 = DiaryEntry("Second Day of Bootcamp", "I'm getting used to the schedule now. I even made some friends.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 25

"""
Given I add two diary entries
and given a words per minute of 5
return that it would take me 5 minutes to read all of my entries
"""

def test_two_entries_5_wpm_returns_5_min_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("First Day of Bootcamp", "Today was an exciting day! It was challenging, but I learned a lot.")
    entry_2 = DiaryEntry("Second Day of Bootcamp", "I'm getting used to the schedule now. I even made some friends.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(5) == 5

"""
Given I add two diary entries
and given a words per minute of 5
and 1 minute
return the instance of a diary entry that is closest to 
but not over the length that the user could read
"""

def test_find_best_entry_for_reading_time_given_two_entries():
    diary = Diary()
    entry_1 = DiaryEntry("First Day of Bootcamp", "Today was an exciting day!")
    entry_2 = DiaryEntry("Second Day of Bootcamp", "I'm getting used to the schedule now. I even made some friends.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(3, 2) == entry_1

    """
Given I add one diary entry
and given the right wpm and time to read that entry
return that entry
"""

def test_find_best_entry_for_reading_time_given_one_perfect_entry():
    diary = Diary()
    entry_1 = DiaryEntry("First Day of Bootcamp", "Today was an exciting day!")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(5, 1) == entry_1

"""
Given I add one diary entry
and given the words per minute and time isn't long enough to read that entry
find_best_entry_for_reading_time returns None
"""

def test_returns_none_when_time_and_wpm_not_enough_to_read_entry():
    diary = Diary()
    entry_1 = DiaryEntry("First Day of Bootcamp", "Today was an exciting day! I'm very happy.")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 2) == None
