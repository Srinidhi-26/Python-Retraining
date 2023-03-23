import sqlite3
from model import City, city_Status


def add_City_Info(n):
    c = 0
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO city
                          (city_name,area_name,pincode) 
                           VALUES 
                          (?,?,?)"""

        data_tuple = (n.city_name,n.area_name,n.pincode,)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()
        c = 1

    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c

def change_City_Info(a,b):
    c = 0
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """update city set city_name = (?) where city_name = (?)"""
        data = (b,a)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            c = 1

        cursor.close()
    

    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    
    return c

def change_Area_Info(a,b):
    c = 0
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """update city set area_name = (?) where area_name = (?)"""
        data = (b,a)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            c = 1
        cursor.close() 
    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    
    return c

def view_City_Info(id):
    el = []
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from city where city_name = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        
        for row in records:
            n = City(row[0],row[1],row[2])
            c = (n.area_name,n.pincode)
            el.append(c)
            
        cursor.close()

    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return el

def pincode_Info(num):
    es = city_Status(0,"Not found",None)
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from city where pincode = ?"""
        cursor.execute(sql_select_query, (num,))
        records = cursor.fetchall()

        for row in records:
            n = City(row[0],row[1],row[2])
            v = (n.city_name,n.area_name)
            es.statuscode = 1
            es.message = "City Found"
            es.cityobj = v
            
            
        cursor.close()

    except sqlite3.Error as error:
        es.message = f"{error}"

    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return es

def sort_City_Info():
    c = []
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM city order by city_name")
        records = cursor.fetchall()
        sqliteConnection.commit()
        
        cursor.close()
        for  row in records:
            n = City(row[0],row[1],row[2])
            c.append(n)

    except sqlite3.Error as error:
        return c
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c

def sort_Area_Info():
    c = []
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM city order by area_name")
        records = cursor.fetchall()
        sqliteConnection.commit()
        
        cursor.close()
        for  row in records:
            n = City(row[0],row[1],row[2])
            c.append(n)

    except sqlite3.Error as error:
        return c
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c

def sort_Pin_Info():
    c = []
    try:
        sqliteConnection = sqlite3.connect('task5.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM city order by pincode")
        records = cursor.fetchall()
        sqliteConnection.commit()
        
        cursor.close()
        for  row in records:
            n = City(row[0],row[1],row[2])
            c.append(n)

    except sqlite3.Error as error:
        return c
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c