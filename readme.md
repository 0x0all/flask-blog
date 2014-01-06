Flask-Blog
=========

My personal blog, wrote it from scratch.  
It's based on Flask and sqlite3 and markdown, powered by Nginx and uwsgi.  
However it's not a static blog.  
I did plan to make it static at first, but abandon it when it generated the ugly code.  


####File Tree

_configure files of Nginx and uwsgi_  
├── conf            
│   ├── nginx.conf
│   └── uwsgi.ini

_sqlite database_
├── db
│   └── posts.db

_log directory_
├── logs
├── readme.md

_python source files_
└── src
    ├── blog
    │   ├── config.py   _blog configs_
    │   ├── config.pyc
    │   ├── db.py
    │   ├── deletepost.py
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── markdown
    │   ├── md2html.py
    │   ├── newpost.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── chess.css
    │   │   │   ├── main.css
    │   │   │   ├── resume.css
    │   │   │   ├── sing.css
    │   │   │   └── space-is-key.css
    │   │   ├── files
    │   │   │   ├── find_your_cetid.zip
    │   │   │   ├── lz-round-gravatar.crx
    │   │   │   ├── th-codes.rar
    │   │   │   ├── th-weibo.rar
    │   │   │   ├── tieba.zip
    │   │   │   └── url-qrcode.crx
    │   │   ├── images
    │   │   │   ├── favicon.png
    │   │   │   ├── github.png
    │   │   │   ├── google.png
    │   │   │   ├── rss.png
    │   │   │   └── twitter.png
    │   │   └── js
    │   │       ├── chess.js
    │   │       ├── sing.js
    │   │       └── space-is-key
    │   │           ├── draw.js
    │   │           └── round-config.js
    │   ├── templates
    │   │   ├── base.html
    │   │   ├── pages
    │   │   │   ├── 404.html
    │   │   │   ├── about
    │   │   │   │   └── index.html
    │   │   │   ├── archives.html
    │   │   │   ├── atom.xml
    │   │   │   ├── home.html
    │   │   │   ├── projects
    │   │   │   │   ├── find_your_cetid.html
    │   │   │   │   ├── index.html
    │   │   │   │   ├── js-toys
    │   │   │   │   │   ├── chess
    │   │   │   │   │   │   └── index.html
    │   │   │   │   │   ├── sing-the-pics
    │   │   │   │   │   │   └── index.html
    │   │   │   │   │   └── space-is-key
    │   │   │   │   │       └── index.html
    │   │   │   │   ├── lz-round-gravatar.html
    │   │   │   │   └── url-qrcode.html
    │   │   │   ├── resume
    │   │   │   │   └── index.html
    │   │   │   ├── robots.txt
    │   │   │   └── tags.html
    │   │   ├── post.html
    │   │   ├── postlist.html
    │   │   └── posts
    │   ├── views.py
    │   └── views.pyc
    └── index.wsgi


