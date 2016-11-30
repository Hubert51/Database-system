"""
This part is most important part in my project part since user can call my
function from this class. So they do not need tp have knowledge about database
and SQL
These codes are the functions part in my database project. The first function is
initial the program. The create_table(self,information)

I need to talk with group members to know what kind of operations they want to 
have, such as finding the average, finding the course. Then I should write such
function for them.

"""

import sqlite3


class DatabaseIO:
    def __init__(self, name):
        """
        In my opinion, this is an initial part. If I have to use variable from
        other class, I can call in this part and then call to the following
        part.
        Some variable must be renamed again.
        """

        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()
        d_table = {}
        

    def create_table1(self):
        table_name = raw_input("Please entre the table name ==> ")
        l = []  # This list stores the info which is used to create table
        while 1 > 0:
            column = raw_input('''Please entre column with this data tpye such as 
INTEGER or TXT (if finish, type: end) ==> ''')
            if column != "end":
                l.append(column)
            else:
                break
        key = raw_input("Please enter the key ==> ")
        num = len(l)        
        command = "CREATE TABLE {:} (".format(table_name)
        
        
        
        for i in l:
            command += "{:} NOT NULL,".format(i)
            
        command += "PRIMARY KEY ({:}))".format(key)
               
        self.cur.execute(command)
        self.con.commit()        
    
    
    def add_data(self):
        table_name = raw_input("Please enter the table name which you want to add data ==> ")
        
        if table_name == "student":
            rin = raw_input("Please entre the Rin ==> ")
            name = raw_input("Please entre the name ==> ")
            user_name = raw_input("Please entre the username ==> ")
            passport = raw_input("Please entre the passport ==> ")
            email = raw_input("Please entre the email ==> ")

            information = (rin, name, user_name, passport, email)
            cur = self.cur.execute('INSERT INTO ' + '"' + table_name + '"' + 'VALUES (?,?,?,?,?)', information)
            self.con.commit()
            
        elif table_name == "course":
            
            course_number = raw_input("Please entre the course_number ==> ")
            time = raw_input("Please entre the time ==> ")  
            rin = raw_input("Please entre the rin ==> ")
            
            information = (course_number,time,rin)
            cur = self.cur.execute('INSERT INTO ' + '"' + table_name + '"' + 'VALUES (?,?,?)', information)            
            
            
            

    def execute(self, string):
        return self.cur.execute(string)

    def fetchall(self):
        table = raw_input("Which table do you want print? ==> ")
        for row in self.cur.execute('SELECT * FROM {:s}'.format(table)):
            print row

