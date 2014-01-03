#!/usr/bin/python
#-*-coding:utf-8-*-
import sqlite3

conn = sqlite3.connect('db/posts.db')
c = conn.cursor()

# c.execute('''CREATE TABLE posts
#             (date text, title text primary key, tags text, preview text)''')

# c.execute("INSERT INTO posts VALUES ('2014-01-03', 'hello-world', ',blog', 'hahahaha')")

row = c.execute("SELECT * FROM posts ORDER BY DATE")
for r in row:
    print r[1]

conn.commit
conn.close()
