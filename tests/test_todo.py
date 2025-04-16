from lib.todo import *

"""
Given a task
check that the task is still incomplete
"""

def test_given_task_check_task_is_incomplete():
    task_1 = Todo("Water the plants")
    assert task_1.complete == False

"""
Given a task
and then marking that task as complete
return that the task is complete by returning True
"""

def test_given_task__then_marking_complete_check_task_is_complete():
    task_1 = Todo("Water the plants")
    task_1.mark_complete()
    assert task_1.complete == True