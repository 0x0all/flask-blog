#-*-coding:utf-8-*-
from flask import render_template, url_for
from blog import blog
import sqlite3


def getDB():
    conn = sqlite3.connect('blog/db/posts.db')
    return conn.cursor()


@blog.route('/')
@blog.route('/home')
def home():
    PAGINATE = 10
    c = getDB()
    posts = c.execute("SELECT * FROM posts ORDER BY date DESC").fetchall()
    num = PAGINATE if len(posts) > PAGINATE else len(posts)
    return render_template('pages/home.html', articles=posts[:num])


@blog.route('/archives')
def archives():
    c = getDB()
    posts = c.execute("SELECT * FROM posts ORDER BY date DESC").fetchall()
    return render_template('pages/archives.html', articles=posts)


@blog.route('/tags/<tag>')
def tags(tag):
    c = getDB()
    posts = c.execute(
        "SELECT * FROM posts WHERE tags like ? ORDER BYdate DESC",
        ('%,{}%'.format(tag),
         )).fetchall()
    return render_template('pages/tags.html', articles=posts)


@blog.route('/blog/<title>')
def index(title):
    return render_template('posts/{}.html'.format(title))


@blog.route('/about/')
def about():
    return render_template('pages/about/index.html')


@blog.route('/projects/', defaults={'path': 'index'})
@blog.route('/projects/<path:path>')
def projects(path):
    try:
        htmlfile = 'pages/projects/{}.html'.format(path)
        return render_template(htmlfile)
    except Exception as e:
        htmlfile = 'pages/projects/{}/index.html'.format(path)
        return render_template(htmlfile)


@blog.route('/resume/')
def resume():
    return render_template('pages/resume/index.html')
