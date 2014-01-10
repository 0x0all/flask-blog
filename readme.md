Flask-Blog
=========

My personal blog, wrote it from scratch.  
It's based on Flask and sqlite3 and markdown, powered by Nginx and uwsgi.  
  
However it's not a static blog.  
I did plan to make it static at first, but abandon it when it generated the ugly code.  

---

In `src/blog`  

create a post:   
    
    python newpost.py post-title

convert it to html:

    python md2html.py markdown/post-title.md

delete a post:

    python deletepost.py markdown/post-title.md



