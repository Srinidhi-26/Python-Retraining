from task import Task, TaskManager, tasks
from tasklogic import updatetask, addtask, viewtask, viewalltasks, removetask
def pres():
    exit = False
    while not exit:
        print("1. Enter Task ID\n2. View All Tasks\n0. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            task_id = int(input("Enter Task ID: "))
            if task_id in tasks.tasks:
                print("1. Update Task\n2. View Task\n3. Remove Task\n0. Main Menu")
                ch = int(input("Enter Your Choice: "))
                if ch == 1:
                    name = input("Enter Task Name: ")
                    desc = input("Enter Description: ")
                    pri = int(input("Enter Priority: "))
                    updatetask(task_id, name,desc,pri)
                    print("Task Updated Successfully")
                if ch == 2:
                    result = viewtask(task_id)
                    print(result)

                if ch == 3:
                    result =removetask(task_id)
                    print(result)
                if ch == 0:
                    pres()
            else:
                name = input("Enter Task Name: ")
                desc = input("Enter Description: ")
                pri = int(input("Enter Priority: "))
                result = addtask(task_id, name, desc, pri)
                print(result)

        elif ch == 2:
            for task in viewalltasks():
                print(task)
        elif ch == 0:
            exit = True
        else:
            print("Invalid Choice")
