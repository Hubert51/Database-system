'''
In part1, I try to understand database in python. How to input data, how to 
operate the data.
@SQL - structured query language(SQL). We use this brand of database because
           it is simple to use and in python3 standard library, we have this 
           module called sqlite3
@The capatial and lower words are almost same. Only need to be careful is table 
 name --> PopByRegion
'''

import sqlite3
con = sqlite3.connect("population.db")          #create a database.

"""
Then we need a cursor.  This keeps track of where we are in the database so 
that if several programs are accessing the database at the same time, the 
database can keep track of who is trying to do what
"""
cur = con.cursor()                              


cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')

#To input the data of the population and area in 2300.
cur = cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Northern Africa",1037463)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Southern Asia",2051941)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Asia Pacific",785468)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Middle East",687630)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Eastern Asia",1362955)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("South America",593121)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Eastern Europen",223427)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("North America",661157)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Western Europen",387933)')
cur = cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')

con.commit                                        #To store the table

# To retrieving data.
cur.execute('SELECT Region, Population FROM PopByRegion') 

#Use print function to test code.
print(cur.fetchone())                             #Test print one value
print(cur.fetchall())                             #Test print all values

cur.execute('select region, population from PopByRegion order by region')

cur.execute('''select region, population from PopByRegion order by population
            DESC''')      # DESC - descending     ASC - ascending

# where conditions are always applied row by row.  
cur.execute('''select region, population from PopByRegion where
            population >1000000 and region < "L"''')


# To update Japan from original to 100600 population
# * - all data from database
# If you want to test code, you can use print(cur.fetchone())

cur.execute("select * from PopByRegion where region = 'Japan'")
cur.execute('''update PopByRegion set Population = 100600
               where Region = "Japan"''')
cur.execute("select * from PopByRegion where Region = 'Japan'")


# Also, we can delete records from database:
# No matter use uppercase or lower case in the quatation
cur.execute('delete from PopByRegion where region < "L"')
cur.execute('select * from popbyregion')
print(cur.fetchall())

# If we want to put the data back to the table
cur.execute('insert into popbyregion values ("Japan",100562)')
cur.execute("select * from popbyregion ")
print(cur.fetchall())

""" To remove an entire table from database,we can use the drop command: 
    drop table TableName. If you do this, all the data from table will lose.
    So it is better to copy before drop sizable data.
"""
#cur.execute('drop table popbyregion')


#If you meet some region which do not have data, you can use null for missing data.
cur.execute('insert into popbyregion values ("Mars",null)')


'''
Some problems in this section: I do not know how to test. I do not know the name
of the test table.

# If you do not want to have a database with null value
cur.execute('create table test (region text not null,population integer)')
'''

"""
Attention: In SQL's view of world. There are three result: True, False, Unknown
           Null represents the last one. However, different databases interpret 
           ambiguities in the SQL standard in different ways. So their handling 
           of Null is not consistent. 
"""

