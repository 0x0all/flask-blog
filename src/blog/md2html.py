#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import sqlite3
import markdown
import datetime
from config import *

# markdown file info
info = {
    'date': '',
    'title': '',
    'tags': ','
    }

# jinja2 syntax to insert to html
tmplSyntax = [
    '{% extends "post.html" %}',
    '{% block post %}',
    '',
    '{% endblock %}'
    ]


def markdownToHtml(mdfile):
    ''' convert .md to .html '''
    text = open(mdfile, 'r').read().decode('utf-8')
    postinfo, content = text.split(INFO_CONTENT_SPLIT)
    infolist = postinfo.split('\n')

    for i in infolist:
        if not i:
            continue
        k, v = i.split(':')
        info[k] = v

    html = markdown.markdown(content).encode('utf-8')
    tmplSyntax[2] = html
    with open('templates/posts/{}.html'.format(info['title']), 'w') as f:
        f.write('\n'.join(tmplSyntax))

    preview = html.split(PREVIEW_MORE_SPLIT[:-1])[0].decode('utf-8')
    c.execute("INSERT OR REPLACE INTO posts VALUES (?, ?, ?, ?)", [info['date'],
                info['title'], ',{},'.format(info['tags']), preview])

    conn.commit()
    conn.close()




if __name__ == '__main__':
    try:
        mdfile = sys.argv[1].strip("'").strip('"')
        conn = sqlite3.connect(DBFILE)
        c = conn.cursor()
        markdownToHtml(mdfile)

    except IndexError:
        print 'Please specific a markdown file'

    except Exception as e:
        print e

    finally:
        exit()
