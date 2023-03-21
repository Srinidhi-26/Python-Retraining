from emplogic import get_employee_details, get_employees_by_dept_id

def pres():
    exit = False
    while not exit:
        print("\nMENU")
        print("1. Get employee details by employee number")
        print("2. Get all employees by department ID")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            emp_no = int(input("Enter employee number: "))
            print(get_employee_details(emp_no))
        elif choice == "2":
            dept_id = int(input("Enter department ID: "))
            print(get_employees_by_dept_id(dept_id))
        elif choice == "0":
            exit == True
        else:
            print("Invalid choice.")
