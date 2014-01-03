#-*-coding:utf-8-*-
from flask import render_template
from blog import blog
import sqlite3

@blog.route('/blog/<title>')
def index(title):
    return render_template('posts/{0}.html'.format(title))
            

@blog.route('/archives')
def archives():
    return render_template('pages/archives.html')


@blog.route('/')
@blog.route('/home')
def home():
    return render_template('pages/home.html')


@blog.route('/about')
def about():
    return render_template('pages/about.html')


@blog.route('/projects')
def projects():
    return render_template('pages/projects.html')


@blog.route('/resume')
def resume():
    return render_template('pages/resume.html')


@blog.route('/tags/<tag>')
def tags(tag):
    
    conn = sqlite3.connect('blog/db/posts.db')
    c = conn.cursor()
    posts = c.execute("SELECT * FROM posts WHERE tags like '%,{0}%' ORDER BY date DESC".format(tag)).fetchall()
    return render_template('pages/tags.html', articles = posts)
