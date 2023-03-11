import sqlite3
import json

conn = sqlite3.connect('ManyStudentsToTeachers.sqlite')
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE);

CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT UNIQUE,
title TEXT UNIQUE);

CREATE TABLE Member (
user_id INTEGER,
course_id INTEGER,
role INTEGER);


''')

file = 'roster_data.json'
str_data = open(file).read()
json_data = json.loads(str_data)

for entry in json_data:
    username = entry[0]
    course = entry[1]
    role = entry[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (username,))
    cur.execute('SELECT id FROM User WHERE name = ?', (username,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title =?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member(user_id, course_id, role)
    VALUES (?,?,?)''', (user_id, course_id, role))

    conn.commit()

sql = '''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;'''
for row in cur.execute(sql):
    print((row[0]))