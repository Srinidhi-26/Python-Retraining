class Employee:
    def __init__(self, emp_no, name, dept_id):
        self.emp_no = emp_no
        self.name = name
        self.dept_id = dept_id

    def __repr__(self):
        return f"Employee No: {self.emp_no}, Name: {self.name}, Dept ID: {self.dept_id}"

class EmployeeStatus:
    def __init__(self, status_code, message, employee_obj):
        self.status_code = status_code
        self.message = message
        self.employee_obj = employee_obj

    def __repr__(self):
        return f"Status Code: {self.status_code}, Message: {self.message}, Employee: {self.employee_obj}"


employees = {    1: Employee(1, "HI", 101),    2: Employee(2, "Hello", 102),    3: Employee(3, "How", 101),    4: Employee(4, "Are", 103),    5: Employee(5, "You", 102)}

