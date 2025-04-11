from lib.todo_tasks_class import *

#Given a name and a task
#returns a list of the tasks added

def test_add_a_task_and_return_list():
    task = TaskManager()
    task.add("Walk the dog")
    assert task.task_list() == ["Walk the dog"]

#Given a name and two tasks
#returns a list of the tasks added

def test_add_two_tasks_and_return_list():
    task = TaskManager()
    task.add("Walk the dog")
    task.add("Water the plants")    
    assert task.task_list() == ["Walk the dog", "Water the plants"]

#Given a name and a task
#removes that task from the list and returns the list without that task

def test_removes_task_and_returns_list_without_task():
    task = TaskManager()
    task.add("Walk the dog")
    task.add("Water the plants")
    task.task_complete("Walk the dog")
    task.task_list() == ["Water the plants"]

#Given a name and a task
#if the task is already in the list, 
# do nothing and return the list with no changes

def test_duplicate_task_doesnt_add_to_list():
    task = TaskManager()
    task.add("Walk the dog")
    task.add("Water the plants")
    task.add("Walk the dog")
    task.task_list() == ["Walk the dog", "Water the plants"]

#Given a name and an empty task
#do not add the empty string to the list, 
# and return the list with no changes

def test_add_empty_string_return_unchanged_list():
    task = TaskManager()
    task.add("Walk the dog")
    task.add("Water the plants")
    task.add("")
    task.task_list() == ["Walk the dog", "Water the plants"]