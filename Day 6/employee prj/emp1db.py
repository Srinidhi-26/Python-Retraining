import sqlite3
from empmodel import Employee, EmployeeStatus
def insertemployee(a):
    try:
        sqliteConnection = sqlite3.connect('emp.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO employee(emp_no,empname,dept_id)VALUES(?,?,?)"""
        data_tuple = (a.emp_no,a.empname,a.dept_id)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def get_employee_details(n):   
     es = EmployeeStatus(0, "Not Found", None)  
     try:        
        sqliteConnection = sqlite3.connect('emp.db')      
        cursor = sqliteConnection.cursor()     
        sql_select_query = """select * from emp where ID = ?"""    
        cursor.execute(sql_select_query,(n,))    
        records = cursor.fetchall()          
        found = False      
        for row in records:     
              found = True         
              e = Employee(row[0], row[1], row[2])    
              es.status_code = 1      
              es.message = "Found"      
              es.employee_obj = e      
              cursor.close()   
     except sqlite3.Error as error:      
        es.message = error    
     finally:     
            if sqliteConnection:     
                sqliteConnection.close()    
     return es


def get_employees_by_dept_id(id): 
    try:
        sqliteConnection = sqlite3.connect('emp.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from emp where deptid = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        list2 =[]
        for row in records:
            v = Employee(row[0], row[1],row[2])    
            list2.append(v)
            return list2
        cursor.close()
            
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return list2
           

