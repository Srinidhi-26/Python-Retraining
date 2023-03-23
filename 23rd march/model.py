class task:
    def __init__(self,id,taskname,description,priority):
        self.id=id
        self.taskname=taskname
        self.description=description
        self.priority=priority

    def __repr__(self):
            return f"Task id: {self.id},\ntask name: {self.taskname},\nDescription: {self.description},\nPriority: {self.priority}\n"