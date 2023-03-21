class Employee:
    def __init__(self, emp_no, name, dept_id):
        self.emp_no = emp_no
        self.name = name
        self.dept_id = dept_id
    
    def __repr__(self):
        return f"Employee No: {self.emp_no}, Name: {self.name}, Dept ID: {self.dept_id}"
    

employees = {
        Employee(1001, "John Smith", 101),
        Employee(1002, "Jane Doe", 102),
        Employee(1003, "Bob Johnson", 101),
        Employee(1004, "Alice Brown", 103),
        Employee(1005, "Tom Wilson", 102)
}


class EmployeeStatus:
    def __init__(self, status_code, message, employee_list):
        self.status_code = status_code
        self.message = message
        self.employee_list = employee_list 
    
    def __repr__(self):
        return f"Status_code: {self.status_code}:, Message: {self.message}: Employee_list: {self.employee_list}"
       