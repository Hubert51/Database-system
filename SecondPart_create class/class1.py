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
        self.d_table = {}
        self.table = ["Grade","course","professor", "student"]
        
    def showTable(self):
        print ""
        print "There are {} tables".format(len(self.table))
        print(self.table)
        print ""
        
    def table_info(self,table_name=""):
        """
        This function tries to get the information about table in database.
        If table exist, function will print the number of columns in table and
        their name.
        """
        if table_name =="":
            table_name = raw_input("Please entre the table name ==> ")
        info = list(self.cur.execute("PRAGMA table_info('{}')".format(table_name)))
        if len(info) == 0:
            print("This table does not exist!")
            print ''
            
        else:
            print "There are {} columns in this table.".format(info[-1][0]+1)
            for r in info:
                print r  
            print ""
    
    
    
    def create_table(self):
        """
        This function is trying to create a table.n
        """
        
        table_name = raw_input("Please entre the table name ==> ")
        l = []  # This list stores the info which is used to create table
        if table_name in self.d_table:
            print "Table already exist in database."
            pass
        
        self.d_table[table_name] = []
        
        while True:
            column = raw_input('''Please entre column with this data tpye such as 
INTEGER or TXT (if finish, type: end) ==> ''')
            if column != "end":
                l.append(column)
                self.d_table[table_name].append(column)
                
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
        table_name = raw_input("Please enter the table name which you want to add data (you can entre end to end process) ==> ")
        while not table_name in self.table:
            if table_name == "end":
                return
            table_name = raw_input("Please enter the table name which you want to add data (you can entre end to end process) ==> ")            
            
        if table_name in self.table:
            
            information = []   # This list is storing the data user add.
            
            # This info is trying to get the number and of name of column 
            # in target table_name.
            info = list(self.cur.execute("PRAGMA table_info('{}')".format(table_name)))   
            num_of_column = info[-1][0]+1 
            for i in range(info[-1][0]+1):
                # To add data into the list information
                data = raw_input("Please entre the {} ==> ".format(info[i][1]))
                information.append(data)
            information = tuple(information)    # Convert list into tuple so we can process the commend.
            
            # This is the format for sqlite.
            values = 'VALUES ({}?)'.format("?,"*(num_of_column-1))   
            cur = self.cur.execute('INSERT INTO ' + '"' + table_name + '"' + values,information)
            self.con.commit()                        
            
            #cur = self.cur.execute('INSERT INTO ' + '"' + table_name + '"' + 'VALUES (?,?,?,?,?)', information)
            # This is the original form of the commend. But it is not strong enough. So I won't use any more.
            
    def execute(self, string):
        return self.cur.execute(string)

    def fetchall(self):
        table = raw_input("Which table do you want print? ==> ")
        for row in self.cur.execute('SELECT * FROM {:s}'.format(table)):
            print row

    def aggregation(self):
        # This function tries to do some calculation including max,min,avg.
        
        self.showTable()        # To let users know how many tables do they have
        table_name = raw_input('''Which table do you want to calculate? ==> ''')
        
        self.table_info(table_name)    # to show the column inside the named table.
        
        # To know which column do user want to calculate
        column = raw_input('''Which column do you want to calculate? ==> ''')
        commend = raw_input('''What kind of calculation do you want to do? 
                            (avg, min, max, sum) ==>''')
        
        if commend == "avg":
            # calculate the average of the data.
            # Now I will compare with total to get a 100 percent average.
            # This is just suitable for Grade table.
            
            # I use query variable to store the query. Then I can use SQL direct.
            # Use this method, I do not worry about the variable in query.
            query_total = "SELECT {} ({}) FROM {}".format(commend,column,table_name)
            query_total_full = "SELECT {} (totalGrade) FROM {}".format(commend,table_name)

            self.cur.execute(query_total)
            total = self.cur.fetchone()   
            
            self.cur.execute(query_total_full)  
            total_full = self.cur.fetchone()
                        
            avg = 100 * total[0] / total_full[0]        # The out put of fetchone() is a tuple. So i need to get data out. 
            
            print("{:.2f}".format(avg))  # To round the float.
        
        if commend == "max" or commend == "min":
            # 这里需要先算出total是不是一样的，一样的话，就直接算min，max。不一样的话， 
            # 先算成百分比，然后再找出min，max