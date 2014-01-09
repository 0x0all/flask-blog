#-*-coding:utf-8-*-
from flask import render_template, url_for
from blog import blog
from config import *
import sqlite3


def getDB():
    conn = sqlite3.connect(DBFILE)
    return conn.cursor()


@blog.route('/')
@blog.route('/blog')
@blog.route('/home')
def home():
    c = getDB()
    posts = c.execute("SELECT * FROM posts ORDER BY date DESC").fetchall()
    num = PAGINATE if len(posts) > PAGINATE else len(posts)
    return render_template('pages/home.html', posts=posts[:num])


@blog.route('/archives')
def archives():
    c = getDB()
    posts = c.execute("SELECT * FROM posts ORDER BY date DESC").fetchall()
    return render_template('pages/archives.html', posts=posts)


@blog.route('/tags/')
@blog.route('/tags/<tag>')
def tags(tag=None):
    c = getDB()

    if not tag:
        posts = c.execute("SELECT * FROM posts ORDER BY date DESC").fetchall()
        tags = set()
        for p in posts:
            for tag in p[2].split(','):
                if tag: tags.add(tag)
        tags = list(tags)
        tags.sort()
        return render_template('pages/tags.html', tags=tags)

    else:
        posts = c.execute(
            "SELECT * FROM posts WHERE tags like ? ORDER BY date DESC",
            ('%,{},%'.format(tag),
             )).fetchall()
        return render_template('pages/subtags.html', posts=posts)


@blog.route('/blog/<title>')
def posts(title):
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


@blog.route('/robots.txt')
def robots():
    return render_template('pages/robots.txt')


from flask import make_response
@blog.route('/atom.xml/')
def Atom():
    c = getDB()
    posts = c.execute("SELECT * FROM posts ORDER BY date DESC LIMIT 10").fetchall()
    response = make_response(render_template('pages/atom.xml', posts=posts))
    response.headers['Content-Type'] = 'application/xml'
    return response


@blog.errorhandler(404)
def Error404(e):
    return render_template('pages/404.html')
