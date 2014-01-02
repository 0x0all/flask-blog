#-*-coding:utf-8-*-
from flask import render_template
from blog import blog

@blog.route('/')
def index():
    user = {'name': 'hand'}
    return render_template('index.html', title = 'Home')
            
