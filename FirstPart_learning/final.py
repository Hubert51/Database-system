"""
This part of the code is try to create two tables in one database file. 
"""

import sqlite3
con = sqlite3.connect("population.db")
cur = con.cursor()
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
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

con.commit
cur.execute("create table PopByCountry(Region text, Country text, Population integer)")
cur.execute("insert into PopByCountry values('Eastern Asia', 'China', 1285238)")
countries = [("Eastern Asia", "DPR Korea", 24056), ("Eastern Asia","Hong Kong (China)", 8764), ("Eastern Asia", "Mongolia", 3407), ("EasternAsia", "Republic of Korea", 41491), ("Eastern Asia", "Taiwan", 1433),("North America", "Bahamas", 368), ("North America", "Canada", 40876),("North America", "Greenland", 43), ("North America", "Mexico", 126875),("North America", "United States", 493038)]
for c in countries:
    cur.execute("insert into popbycountry values (?,?,?)",(c[0],c[1],c[2]))

con.commit()

cur.execute("""select PopByRegion.Region, PopByCountry.Region
               from   PopByRegion inner join PopByCountry
               where  (PopByRegion.Region = PopByCountry.Region)
               and    (PopByRegion.Population >1000000)""")
print(cur.fetchall())
