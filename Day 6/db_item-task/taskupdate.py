import sqlite3

def updateSqliteTable(taskid, taskname, priority):
    try:
        sqliteConnection = sqlite3.connect('test5.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update task set taskname = ? where taskid = ?"""
      
        data = (taskname, taskid)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            print("update successful")
        else:
            print("no rows where found in the table matching the where condition")


        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

updateSqliteTable(101,'Ruby')