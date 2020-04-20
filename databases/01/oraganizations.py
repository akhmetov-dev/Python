import sqlite3

conn = sqlite3.connect('Organizations.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')

if len(fname) == 0 :
    fname = 'mbox.txt'

try :
    fh = open(fname)
except :
    print("Something wrong.")
    quit()

for line in fh :
    if "From: " in line :
        email = line.split()
        domain = email[1].split("@")[1]
        cur.execute("SELECT count FROM Counts WHERE org = ?", (domain, ))
        row = cur.fetchone()

        if row is None :
            cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (domain, ))
        else :
            cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (domain, ))
        conn.commit()

print(cur.execute("SELECT * FROM Counts"))
cur.close()
