class Task:
    def __init__(self, task_id, name, description, priority):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.task_id} :  {self.name}  {self.description}  {self.priority}"

class TaskManager:
    def __init__(self):
        self.tasks = {}


tasks = TaskManager()
