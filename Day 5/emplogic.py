from empcls import employees, EmployeeStatus
def get_employee_details(emp_no):
     if emp_no in employees:
        return EmployeeStatus(200,'Employee found', [employees[emp_no]])
     else:
        return EmployeeStatus(404, "Employee not found", None)

def get_employees_by_dept_id(dept_id):
    dept_employees = []
    for emp_no, emp in employees.items():
        if emp.dept_id == dept_id:
            dept_employees.append(str(emp))
    if dept_employees:
        return "\n".join(dept_employees)
    else:
        return "No employees found for the given department ID"

   


