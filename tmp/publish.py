#!/usr/bin/python
#-*-coding:utf-8-*-
import sqlite3

PAGINATE = 10

if __name__ == '__main__':
    conn = sqlite3.connect('db/posts.db')
    c = conn.cursor()
    posts = c.execute("SELECT * FROM posts ORDER BY date DESC").fetchall()

    #home.html
    num = PAGINATE if len(posts) > PAGINATE else len(posts)
    content = ''
    for n in xrange(num):
        post = posts[n]
        paragraph = ''
        # paragraph += post[1].join(['<h3>', '</h3>'])
        # paragraph = paragraph.join(['<a href="/blog/{0}">'.format(post[1]), '</a>'])
        paragraph += post[0].join(['<span class="aldate">', '</span><br/>'])
        paragraph += post[3].join(['<div class="preview">', '</div><br/>'])
        paragraph += '<a class="readmore" href="/blog/{0}">read more</a>'.format(post[1])
        paragraph = paragraph.join(['<div class="p">', '</div>'])
        paragraph += '<hr color="silver">\n'
        content += paragraph

    with open('templates/pages/home.html', 'w') as f:
        f.write('{% extends "articlelist.html" %}\n')
        f.write('{% block articlelist %}\n')
        f.write(content.encode('utf-8'))
        f.write('{% endblock %}\n')
    
    #archives.html
    titles = ''
    for p in posts:
        paragraph = ''
        paragraph += p[0].join(['<span class="aldate">', '</span><br/>'])
        paragraph += p[1].join(['<h2 class="altitle">', '</h2>'])
        paragraph = paragraph.join(['<a href="/blog/{0}">'.format(p[1]), '</a>'])
        paragraph = paragraph.join(['<div class="p">', '</div>'])
        titles += paragraph

    with open('templates/pages/archives.html', 'w') as f:
        f.write('{% extends "articlelist.html" %}\n')
        f.write('{% block articlelist %}\n')
        f.write(titles.encode('utf-8'))
        f.write('{% endblock %}\n')



