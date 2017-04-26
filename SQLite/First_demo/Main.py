import class1
import sqlite3

"""
This process is to start the class. All of the following steps should use this
start. And following several steps have different usages
start = class1.DatabaseIO("Student123.db")
start.create_table1()
start.add_data()                         # ADD DATA
start.execute('SELECT * FROM cs1100')    # select all the data from table
start.fetchall()                         # Read all line from table
start.fetchone()                         # Read one line from table
"""
start = class1.DatabaseIO("example.db")

start.create_table1()

start.add_data()                         # ADD DATA

start.execute('SELECT * FROM student')    # select all the data from table

start.fetchall()

