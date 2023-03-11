import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('musicaltracksdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE Album (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
artist_id INTEGER,
title TEXT UNIQUE
);

CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE,
album_id INTEGER,
genre_id INTEGER, 
len INTEGER, rating INTEGER, count INTEGER
);

''')

file = 'Library.xml'
tree = ET.parse(file)
data = tree.findall('dict/dict/dict')

def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

for entry in data:
    if (lookup(entry, 'Track ID') is None):
        continue
    
    track_title = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup (entry, 'Track Count')

    if track_title is None or artist is None or album is None or genre is None:
        continue
    
    #print (track_title, artist, genre, album, length, rating, count)

    cur.execute(''' INSERT OR IGNORE INTO Artist (name) VALUES (?) ''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (artist_id, title) 
    VALUES (?,?)''', (artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track 
    (title, album_id, genre_id, len, rating, count)  
    VALUES (?,?,?,?,?,?)
    ''', (track_title, album_id, genre_id, length, rating, count))

    conn.commit()


sql = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''

for row in cur.execute(sql):
    print((row[0]), row[1], row[2], row[3])