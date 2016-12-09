import class1
import sqlite3


"""
This process is to start the class. All of the following steps should use this
start. And following several steps have different usages
start = class1.DatabaseIO("Student123.db")
start.table_info                         # Check whether table is exist or not
start.create_table1()
start.add_data()                         # ADD DATA
start.execute('SELECT * FROM cs1100')    # select all the data from table
start.fetchall()                         # Read all line from table
start.fetchone()                         # Read one line from table
"""
start = class1.DatabaseIO("example2.db")
    
commend = ""

while commend != "end":
    
    commend = raw_input("what do you want to do? ('create', 'add', 'execute', 'fetch' or 'end'): ")
    if commend == "checktable":
	start.table_info()
	
    elif commend == "create":
	start.create_table()
	
    
    elif  commend == "add":
	start.add_data()                         # ADD DATA

    elif  commend == "execute":
	start.execute('SELECT * FROM student')    # select all the data from table

    elif commend == "fetch":
	start.fetchall()










