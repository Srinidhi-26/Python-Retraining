from tasklogic import addTask,present,updateTask,viewTask,removeTask 
from task import task
def pres(): 
    exit = False
    while not exit:
        print("0.Exit\n1. Enter Task ID")
        ch= int(input("Enter U r Choice: "))
        if ch==0:
             exit=True
             if ch==1: 
                 id=int(input("Enter the Task ID: "))
                 res=present(id)
                 print(res)
                 print("0. Go back to menu\n1. Add task information\n2. update task information\n3. view Task information\n4. Remove Task Information")
                 ch=int(input("Enter u r Option: "))
             if ch==1:
                 id=int(input("Enter the id: "))
                 nam=input("Enter the Task name: ") 
                 des=input("Enter the description: ")
                 pri=int(input("Value the priority: "))
                 x=task(id,nam,des,pri)
                 res=addTask(x)
                 print(res,"\n")
             if ch==2:
                id=int(input("Enter the id: "))
                nam=input("Enter the Task name to update: ") 
                des=input("Enter the description to update: ")
                pri=int(input("Value the priority to update: "))
                x=task(id,nam,des,pri)
                res=updateTask(x)
                print(res,"\n")
             if ch==3:
                id=int(input("Enter the Task id to view the information: "))
                res=viewTask(id)
                print(res,"\n")
             if ch==4:
                id=int(input("Enter the Task id to remove: "))
                res=removeTask(id)
                print(res,"\n")