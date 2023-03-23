from emploic1 import get_employee_details, get_employees_by_dept_id, insertemployee
def pres():
    exit = False    
    while not exit:       
         print("1. View Specific\n2. Get employees by department ID\n0. Exit")      
         choice = input("Enter your choice: ")      
         if choice == "1":        
                n = int(input("Enter employee ID:"))         
                res = get_employee_details(n)        
                if res.status_code == 0:             
                       print("No employee found")      
                else:           
                         print("Employee Found",res.employee_obj)      
         
         elif choice == "2":          
              dept_id = int(input("Enter department ID: "))        
              v= get_employees_by_dept_id(dept_id) 
              if len(v)==0:
                   print('no employees found in dept')
              else:
                   for emp in v:
                        print(v)    
   
         elif choice == "0":            
            exit == True      
            
    else:   
       print("Invalid choice")