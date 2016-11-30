import sqlite3

class DatabaseIO:
    l12 = [1, 2, 3]
    d_table = {}

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
        i = 0
        l = []  # This list stores the info which is used to create table
        l2 = []  # This list stores the table info which will be useful when we need to know the columns of  table
        d_table = dict()
        check = True
        while check:
            column = raw_input('''Please entre column with this data tpye such as 
INTEGER or TXT (if finish, type: end) ==> ''')
            if column != "end":
                l.append(column)
                l2.append(column)
            else:
                break
        d_table[table_name] = l2
        key = raw_input("Please enter the key ==> ")
        
        command = "CREATE TABLE {:} (".format(table_name)
        for i in l:
            command += "{:} NOT NULL,".format(i)
            
        command += "PRIMARY KEY ({:}))".format(key)
               
        self.cur.execute(command)
        self.con.commit()

