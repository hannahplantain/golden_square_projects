import pytest
from lib.diary import Diary


"""
Inittially has an empty list of entries
"""

def test_empty_list_return():
    diary = Diary()
    assert diary.all() == []

"""
Inittially word count is 0 when no entries
"""

def test_counts_words_in_entries():
    diary = Diary()
    assert diary.count_words() == 0

"""
Initially reading time should raise an error
"""

def test_reading_time_no_entries_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2) 
        assert str(err.value) == "No entries added yet."