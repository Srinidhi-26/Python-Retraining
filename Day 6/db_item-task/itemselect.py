import sqlite3

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('test4.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from item where itmno = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("itmno  = ", row[0])
            print("itmname  = ", row[1])
            print("price  = ", row[2])
            print("category  = ", row[3])
           
            
        else:
            print("no itmno found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(4)