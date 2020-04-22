import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect("tracks.sqlite")
cur = conn.cursor()

def lookup(song, key):
    found = False
    for attr in song:
        if found : return attr.text
        if attr.tag == 'key' and attr.text == key :
            found = True
    return None

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

fname = input("Input filename:")

if len(fname) == 0 :
    fname = "Library.xml"

try :
    content = ET.parse(fname)
except :
    print("Something wrong.")
    quit()

root = content.getroot()
songs = root.findall("dict/dict/dict")

for song in songs :
    if ( lookup(song, 'Track ID') is None ) : continue
    name = lookup(song, 'Name')
    artist = lookup(song, 'Artist')
    album = lookup(song, 'Album')
    genre = lookup(song, 'Genre')
    length = lookup(song, 'Total Time')
    rating = lookup(song, 'Rating')
    count = lookup(song, 'Play Count')
    print("Name:", name)
    print("Artist:", artist)
    print("Album:", album)
    print("Genre:", genre)
    print("Length:", length)
    print("Reting:", rating)
    print("Count:", count, "\n")

    if name is None or artist is None or album is None or genre is None:
        continue

    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist, ))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)", (album, artist_id))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album, ))
    album_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre, ))
    cur.execute("SELECT id FROM Genre WHERE name = ?", (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count)
    VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))

    conn.commit()
