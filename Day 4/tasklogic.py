from task import Task
from task import tasks

def updatetask(task_id, name, desc, pri):
    task = tasks.tasks.get(task_id)
    task.name = name
    task.description = desc
    task.priority = pri
    return

def addtask(task_id, name, desc, pri):
    task = Task(task_id, name, desc, pri)
    tasks.tasks[task_id] = task
    return task

def viewtask(task_id):
    task = tasks.tasks.get(task_id)
    return task

def viewalltasks():
    return (f"{task_id} : {task.name}  {task.description}  {task.priority} " for task_id, task in
            tasks.tasks.items())

def removetask(task_id):
    del tasks.tasks[task_id]
