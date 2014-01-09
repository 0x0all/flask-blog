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
        'tags': ''
    }


def newPost(title):
    date = datetime.date.today().__str__()
    info['title'] = title
    info['date'] = date

    with open('markdown/{}.md'.format(title), 'w') as f:
        for key in info:
            f.write(':'.join([key, info[key]]) + '\n')
        f.write('#\n'.join([INFO_CONTENT_SPLIT, PREVIEW_MORE_SPLIT]))

    print 'markdown/{}.md created!'.format(title)
    exit(0)


if __name__ == '__main__':
    try:
        title = sys.argv[1].strip("'")
        conn = sqlite3.connect(DBFILE)
        c = conn.cursor()
        newPost(title)
        exit(0)
        
    except IndexError as e:
        print 'Please specific a title'

    except Exception as e:
        print e
        exit(-1)
