

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

```python
# EXAMPLE

class TaskManager:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   stores the user's tasks
        pass 

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass 

    def task_list(self):
        # Parameters:
        #   none
        # Returns:
        #   a list of the tasks already added
        # Side-effects:
        #   Throws an exception if there are no tasks in the list
        pass 

    def task_complete(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   none
        # Side-effects:
        #   removes that task from the list
```

## 3. Create Examples as Tests

``` python
# EXAMPLE

"""
Given a name and a task
#returns a list of the tasks added
"""
task = TaskManager()
task.add("Walk the dog")
task.task_list() # => ["Walk the dog"]

"""
Given a name and two tasks
#returns a list of the tasks added
"""
task = TaskManager()
task.add("Walk the dog")
task.add("Water the plants")
task.task_list() # => ["Walk the dog", "Water the plants"]

"""
Given a name and a task
#removes that task from the list and returns the list without that task
"""
task = TaskManager()
task.add("Walk the dog")
task.add("Water the plants")
task.task_complete("Walk the dog")
task.task_list() # => ["Water the plants"]

"""
Given a name and a task
#if the task is already in the list, do nothing and return the list with no changes
"""
task = TaskManager()
task.add("Walk the dog")
task.add("Water the plants")
task.add("Walk the dog")
task.task_list() # => ["Walk the dog", "Water the plants"]


"""
Given a name and an empty task
#do not add the empty string to the list, and return the list with no changes
"""
task = TaskManager()
task.add("Walk the dog")
task.add("Water the plants")
task.add("")
task.task_list() # => ["Walk the dog", "Water the plants"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
