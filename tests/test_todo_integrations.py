from lib.todo_list import *
from lib.todo import *

"""
Given an incomplete todo
add it to the todo list
return the todo as a list of incomplete todos
"""

def test_add_a_todo_return_list_of_incompleted_todo():
    todo_list = TodoList()
    item_1 = Todo("Water the plants")
    todo_list.add(item_1)
    assert todo_list.incomplete() == [item_1]

"""
Given multiple incomplete todo tasks
add them to the todo list
return a list of the incomplete todos
"""
def test_add_multiple_todos_return_list_of_all_incompleted_todos():
    todo_list = TodoList()
    item_1 = Todo("Water the plants")
    item_2 = Todo("Shop for groceries")
    item_3 = Todo("Call my mom")
    todo_list.add(item_1)
    todo_list.add(item_2)
    todo_list.add(item_3)
    assert todo_list.incomplete() == [item_1, item_2, item_3]


"""
Given a todo
add it to the todo list
mark that todo as completed
return a list of the completed todos with just that item
"""

def test_add_a_todo_mark_it_complete_return_list_of_completed_todos():
    todo_list = TodoList()
    item_1 = Todo("Water the plants")
    todo_list.add(item_1)
    item_1.mark_complete()
    assert todo_list.complete() == [item_1]

"""
Given multiple incomplete todo tasks
add them to the todo list
mark only one as completed
return a list of the one incomplete todo
"""

def test_add_multiple_todos_mark_one_complete_return_list_of_one_complete_todo():
    todo_list = TodoList()
    item_1 = Todo("Water the plants")
    item_2 = Todo("Shop for groceries")
    item_3 = Todo("Call my mom")
    todo_list.add(item_1)
    todo_list.add(item_2)
    todo_list.add(item_3)
    item_2.mark_complete()
    assert todo_list.complete() == [item_2]

"""
Given one task in the todo list
call the give_up method to change it to completed
return the list of completed todos
"""

def test_give_a_todo_call_give_up_return_same_todo_as_completed():
    todo_list = TodoList()
    item_1 = Todo("Water the plants")
    todo_list.add(item_1)
    todo_list.give_up()
    assert todo_list.complete() == [item_1]

    """
Given multiple tasks in the todo list
call the give_up method to change them to completed
return the list of completed todos
"""

def test_add_multiple_todos_call_give_up_return_all_as_completed():
    todo_list = TodoList()
    item_1 = Todo("Water the plants")
    item_2 = Todo("Shop for groceries")
    item_3 = Todo("Call my mom")
    todo_list.add(item_1)
    todo_list.add(item_2)
    todo_list.add(item_3)
    todo_list.give_up()
    assert todo_list.complete() == [item_1, item_2, item_3]