import sqlite3
conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

##cur.execute('SELECT * FROM LTE')
##for row in cur :
##    print row[0], row[1], row[7]
##
cur.execute('SELECT substr(MOI,1,length(MOI) - 11) FROM Prach')
for row in cur :
    print row[0]

print
print
print

cur.execute('SELECT * FROM Prach inner join LTE on substr(Prach.MOI,1,length(Prach.MOI) - 11) == LTE.MOI')
for row in cur :
    print row[0], row[1], row[7]

print
print
print

# this is the sqlite equivalent of desc table;
connection = sqlite3.connect('music.sqlite3')
connection.row_factory = sqlite3.Row
cursor = connection.execute('select * from LTE')

row = cursor.fetchone()
names = row.keys()
print names
conn.commit()
cur.close()
