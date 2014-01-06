#-*-coding:utf-8-*-
from flask import Flask

blog = Flask(__name__)

# settings here
blog.PAGINATE = 10
blog.DBFILE = '/home/yakiang/Templates/flask-blog/db/posts.db'

import views
