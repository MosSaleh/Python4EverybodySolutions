import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = ('mbox.txt')
fh = open(fname)

count = dict()
for line in fh:
    email = re.findall('^From\s\S+@(\S+)\s', line)
    if len(email) != 1:
        continue
    else:
        email = str(email)
        email = email.strip("['']")
        count[email] = count.get(email, 0) + 1

for org,count in count.items():

    cur.execute('''INSERT INTO Counts (org, count) 
    VALUES (?, ?)''', (org, count))
    conn.commit()

sql = ('SELECT * FROM Counts ORDER BY count DESC')
for row in cur.execute(sql):
    print((row[0]), row[1])

