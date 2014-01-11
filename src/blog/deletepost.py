#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import os
import sqlite3
from config import *


def deletePost(mdfile):
    ''' delete a post '''
    title = mdfile.split('/')[-1].split('.')[0]
    os.remove(mdfile)
    os.remove('templates/posts/{}.html'.format(title))

    c.execute('DELETE FROM posts WHERE title=?', (title,))
    conn.commit()
    conn.close()




if __name__ == '__main__':
    try:
        mdfile = sys.argv[1].strip("'").strip('"')
        conn = sqlite3.connect(DBFILE)
        c = conn.cursor()
        deletePost(mdfile)

    except IndexError as e:
        print 'Please specific an post file(md) to delete'

    except Exception as e:
        print e

    finally:
        exit()
