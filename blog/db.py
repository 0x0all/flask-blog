#!/usr/bin/python
#-*-coding:utf-8-*-
import sqlite3

conn = sqlite3.connect('db/posts.db')
c = conn.cursor()

# c.execute('''CREATE TABLE posts
#             (date text, title text, tags text, preview text)''')

# c.execute("INSERT INTO posts VALUES ('2014-01-03', 'hello-world', ',blog', 'hahahaha')")

row = c.execute("SELECT * FROM posts")
for r in row:
    print r

conn.commit
conn.close()
