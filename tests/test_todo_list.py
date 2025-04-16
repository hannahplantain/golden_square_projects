from lib.todo_list import *

"""
Testing the init of the class with an empty list
"""

def test_instantiating_the_class_with_empty_list():
    todo_list = TodoList()
    assert todo_list.list_of_todo == []

