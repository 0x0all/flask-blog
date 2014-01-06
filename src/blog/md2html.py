#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import sqlite3
import markdown
import datetime
from config import *

info = {
        'date': '',
        'title': '',
        'tags': ','
    }

def markdownToHtml(mdfile):
    text = open(mdfile, 'r').read().decode('utf-8')
    postinfo, content = text.split(INFO_CONTENT_SPLIT)
    infolist = postinfo.split('\n')
    
    for i in infolist:
        if not i: continue
        k, v = i.split(':')
        info[k] = v

    html = markdown.markdown(content).encode('utf-8')
    with open('templates/posts/{}.html'.format(info['title']), 'w') as f:
        f.write('\n'.join(['{% extends "article.html" %}', '{% block article %}',
            html, '{% endblock %}']))

    preview = html.split(PREVIEW_MORE_SPLIT[:-1])[0].decode('utf-8')
    c.execute("INSERT OR REPLACE INTO posts VALUES (?, ?, ?, ?)", [info['date'],
        info['title'], info['tags'], preview])

    conn.commit()
    conn.close()




if __name__ == '__main__':
    try:
        mdfile = sys.argv[1].strip("'")
        conn = sqlite3.connect(DBFILE)
        c = conn.cursor()
        markdownToHtml(mdfile)
        exit(0)

    except IndexError as e:
        print 'Please specific a markdown filename'

    except Exception as e:
        print e
        exit(-1)
