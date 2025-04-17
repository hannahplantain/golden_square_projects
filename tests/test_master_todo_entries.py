from lib.master_diary_classes import *

"""
Given a new todo item
check that the instance was created
"""

def test_add_todo_item_create_instance():
    item_1 = TodoEntries("Water the plants")
    assert item_1.todo == "Water the plants"