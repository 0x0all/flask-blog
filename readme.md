Flask-Blog
=========

My personal blog, wrote it from scratch.  
It's based on Flask and sqlite3 and markdown, powered by Nginx and uwsgi.  
However it's not a static blog.  
I did plan to make it static at first, but abandon it when it generated the ugly code.  


##File Tree


|--- conf            .....  __configure files of Nginx and uwsgi__      
|   |--- nginx.conf     
|   |--- uwsgi.ini      
|--- db              .....  __sqlite database__     
|   └--- posts.db      
|--- logs            .....  __log directory__      
|--- readme.md      
|--- src             .....  __python source files__  
    |--- blog      
    |   |--- config.py           .....  __blog configs__      
    |   |--- deletepost.py       .....  __for delete posts__  
    |   |--- __init__.py      
    |   |--- markdown            .....  __markdown files directory__  
    |   |   |---   
    |   |--- md2html.py          .....  __for converting markdown to html file__  
    |   |--- newpost.py          .....  __for creating new post__  
    |   |--- static      
    |   |   |--- css      
    |   |   |   |--- main.css      
    |   |   |--- files           .....  __static files directory__  
    |   |   |   |---   
    |   |   |--- images      
    |   |   |   |--- favicon.png      
    |   |   |--- js      
    |   |       └---   
    |   |--- templates      
    |   |   |--- base.html       .....  __basic templates__  
    |   |   |--- post.html      
    |   |   |--- postlist.html      
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
    |   |   |--- posts      
    |   |       |---             .....  __articles (html)__  
    |   |--- views.py            .....  __flask views__  
    |--- index.wsgi      
  
  
