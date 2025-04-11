class TaskManager:
    
    def __init__(self):
        self.tasks = []

    def add(self, task):
        if task not in self.tasks and task != "":
            self.tasks.append(task)

    def task_list(self):
        return self.tasks
    
    def task_complete(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
