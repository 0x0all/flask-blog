Flask-Blog
=========

My personal blog, wrote it from scratch.  
It's based on Flask and sqlite3 and markdown, powered by Nginx and uwsgi.  
However it's not a static blog.  
I did plan to make it static at first, but abandon it when it generated the ugly code.  


##File Tree


|--- conf            _configure files of Nginx and uwsgi_      
|   |--- nginx.conf     
|   |--- uwsgi.ini      
|     
|--- db              _sqlite database_     
|   └--- posts.db      
|     
|--- logs            _log directory_      
|     
|--- readme.md      
|     
|--- src             _python source files_  
    |--- blog      
    |   |--- config.py           _blog configs_      
    |   |     
    |   |--- deletepost.py       _for delete posts_  
    |   |     
    |   |--- __init__.py      
    |   |     
    |   |--- markdown            _markdown files directory_  
    |   |   |---   
    |   |     
    |   |--- md2html.py          _for converting markdown to html file_  
    |   |     
    |   |--- newpost.py          _for creating new post_  
    |   |     
    |   |--- static      
    |   |   |     
    |   |   |--- css      
    |   |   |   |--- main.css      
    |   |   |     
    |   |   |--- files           _static files directory_  
    |   |   |   |---   
    |   |   |     
    |   |   |--- images      
    |   |   |   |--- favicon.png      
    |   |   |     
    |   |   |--- js      
    |   |       └---   
    |   |     
    |   |--- templates      
    |   |   |       
    |   |   |--- base.html       _basic templates_  
    |   |   |--- post.html      
    |   |   |--- postlist.html      
    |   |   |     
    |   |   |--- pages      
    |   |   |   |--- 404.html      
    |   |   |   |--- about      
    |   |   |   |   |--- index.html      
    |   |   |   |--- archives.html      
    |   |   |   |--- atom.xml      
    |   |   |   |--- home.html      
    |   |   |   |--- projects      
    |   |   |   |   |--- index.html      
    |   |   |   |--- resume      
    |   |   |   |   |--- index.html      
    |   |   |   |--- robots.txt      
    |   |   |   |--- tags.html      
    |   |   |     
    |   |   |--- posts      
    |   |       |---             _articles (html)_  
    |   |         
    |   |--- views.py            _flask views_  
    |     
    |--- index.wsgi      
  
  
