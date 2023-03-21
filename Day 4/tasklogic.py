d1={}
def present(id):
    if id in d1.keys():
        print()
        return "Present, value =", d1[id]
    else:
        return "Not present\n"
    
def addTask(x):
    if x.id in d1:
        return "This id already present",1
    else:
        d1[x.id]={x.taskname,x.description,x.priority}
        return d1
    
def updateTask(x):
    if x.id not in d1:
        return "This id is not present",1
    else:d1[x.id]={x.taskname,x.description,x.priority}
    return d1

def viewTask(id):
    return d1[id]

def removeTask(id):
    return "Removed",d1.pop(id)