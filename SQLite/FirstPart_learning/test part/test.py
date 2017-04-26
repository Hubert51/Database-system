"""
I created a population.db and stored two tables which is information about 
population in different area inside this file. This python code is try to 
test whether I succeed or not.
"""

import sqlite3
con = sqlite3.connect("population.db")
cur = con.cursor()
cur.execute("select * from PopByRegion ")
print(cur.fetchall())
