# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.list_of_todo = []

    def add(self, todo):
        self.list_of_todo.append(todo)

    def incomplete(self):
        return [task for task in self.list_of_todo if task.complete == False]

    def complete(self):
        return [task for task in self.list_of_todo if task.complete == True]
            

    def give_up(self):
        for task in self.list_of_todo:
                task.mark_complete()