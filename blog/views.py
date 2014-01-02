#-*-coding:utf-8-*-
from flask import render_template
from blog import blog

@blog.route('/')
def index():
    return render_template('posts/hello-world.html')
            
