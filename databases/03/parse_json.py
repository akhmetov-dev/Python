import json
import sqlite3

conn = sqlite3.connect("courses.sqlite")
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id)
    );
''')

fname = input ("Enter db name:")
if len(fname) == 0 :
    fname = "roster_data.json"

try :
    content = open(fname).read()
except :
    print("Something wrong.")
    quit()

json_content = json.loads(content)

for person in json_content :
    user_name = person[0]
    course_title = person[1]
    member_role = person[2]

    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (user_name, ))
    cur.execute("SELECT id FROM User WHERE name = ?", (user_name, ))
    user_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (course_title, ))
    cur.execute("SELECT id FROM Course WHERE title = ?", (course_title, ))
    course_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)", (user_id, course_id, member_role))
    conn.commit()
