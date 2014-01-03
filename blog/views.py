#-*-coding:utf-8-*-
from flask import render_template
from blog import blog

@blog.route('/blog/<title>')
def index(title):
    return render_template('posts/{0}.html'.format(title))
            
