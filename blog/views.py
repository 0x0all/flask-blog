#-*-coding:utf-8-*-
from blog import blog

@blog.route('/')
@blog.route('/index')
def index():
    return 'Hello Flask'
