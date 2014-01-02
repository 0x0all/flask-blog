#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import glob
import sqlite3
import markdown
import datetime

info = {
        'date': '',
        'title': '',
        'tags': '',
        'headings': ''
        }


def newPost():
    try:
        title = arguments[1].strip("'")
        date = datetime.date.today().__str__()
        info['title'] = title
        info['date'] = date
        with open('markdown/{0}.md'.format(title), 'w') as f:
            for key in info:
                f.write(':'.join([key, info[key]]) + '\n')
            f.write('<!---->\n')

        print 'markdown/{0}.md created!'.format(title)
        exit(0)

    except IndexError:
        print "Please specify a title."
        exit(-1)
    except Exception, e:
        print e
        exit(-1)


def markdownToHtml():
    try:
        mdfilename = arguments[1].strip("'")
        text = open(mdfilename, 'r').read().decode('utf-8')
        postinfo, content = text.split('<!---->')
        infolist = postinfo.split('\n')
        for i in infolist:
            if not i: continue
            k, v = i.split(':')
            info[k] = v
        html = markdown.markdown(content).encode('utf-8')
        with open('templates/posts/{0}.html'.format(info['title']), 'w') as f:
            f.write('{% extends "base.html" %}\n')
            f.write('{% block article %}\n')
            f.write(html)
            f.write('\n{% endblock %}\n')

    except IndexError:
        print "I don't know which markdown file to convert."
        exit(-1)
    

whichToRun = {
        'new_post': newPost,
        'md2html': markdownToHtml
        }


if __name__ == '__main__':
    arguments = sys.argv[1:]
    func = whichToRun[arguments[0]]
    func()
