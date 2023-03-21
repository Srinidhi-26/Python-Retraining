class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_roll_no(self):
        return self.roll_no

my_student = Student("John", 21, "A001")

print(my_student.get_name()) 
print(my_student.get_age()) 
print(my_student.get_roll_no()) 
