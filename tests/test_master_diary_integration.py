from lib.master_diary_classes import *

"""
Given a new diary entry
add it into the diary
"""

def test_create_diary_entry_add_to_diary():
    diary = MasterDiary()
    entry_1 = DiaryEntries("First Day", "I had a great first day!")
    diary.add_diary_entry(entry_1)
    assert diary.secret_diary == [entry_1]

"""
Given a new todo list item
add it to the todo list
"""

def test_create_todo_item_add_to_todo_list():
    diary = MasterDiary()
    item_1 = TodoEntries("Water the plants")
    diary.add_todo_entry(item_1)
    assert diary.todo_list == [item_1]

"""
Given a specific diary entry
return the title and contents in a nice format
"""

def test_read_specific_diary_entry():
    diary = MasterDiary()
    entry_1 = DiaryEntries("First Day", "I had a great first day!")
    assert diary.read_past_entry(entry_1) == "First Day: I had a great first day!"

"""
Given a number of minutes and a wpm
and given three diary entries
return a diary entry that the user can read in that amount of time
"""

def test_given_minutes_and_wpm_choose_best_diary_entry_to_read_return_formatted():
    diary = MasterDiary()
    entry_1 = DiaryEntries("First Day", "one two three")
    entry_2 = DiaryEntries("Second Day", "one two three four five six seven eight")
    entry_3 = DiaryEntries("Third Day", "one two three four five six seven eight nine ten")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    diary.add_diary_entry(entry_3)
    assert diary.read_time_efficient_entry(2, 2) == entry_1

    """
    Given a list of diary entries
    with phone numbers inside
    return a list of those phone numbers as strings
    """

def test_return_all_phone_numbers_in_diary_entries():
    diary = MasterDiary()
    entry_1 = DiaryEntries("First day", "my new friend has a number: 07706123456")
    entry_2 = DiaryEntries("Second Day", "one two three four five six seven eight")
    entry_3 = DiaryEntries("Third day", "another 2 numbers, 07756435797 and 07790876540")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    diary.add_diary_entry(entry_3) 
    assert diary.list_of_contact_numbers() == ["07706123456", "07756435797", "07790876540"]
