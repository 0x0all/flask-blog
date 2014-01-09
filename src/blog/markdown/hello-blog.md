date:2013-04-19
tags:blog,ruby,octopress
title:hello-blog
<!---->
#Hello Blog

折腾了一下午和一晚上终于把基于github和Octopress的博客搭了起来。  
之前也知道有基于github的博客但一直以为很高端，直到看到周围有个同学也搞出来了才决定自己也来试一下。  
现在回想真的不难，只不过每一步都可能出现一些意想不到的能让你google上两个小时都不一定能解决的问题。。

<!--more-->
在个人github那儿建立username.github.io这个repo后。在本地把Octopress的项目clone下来。  
进入这个文件夹，依次

    gem install bundler   
    bundle install    
    rake install   

最大问题就可能出现在这里。  
可能你没装ruby，可能ruby版本不对，可能没装rvm，可能没有gem。  
像我，没有ruby基础在这里就停滞了好久。  
解决了ruby版本后要解决rvm的requirements，然后 bundle install 出现无法安装RedCloth问题，google好久最后安装ruby-dev解决。  
之后就没大问题了。 

自定义域名也很简单。之前一直梦想买这个域名，直到今天才出手。  
无奈没有信用卡，又找不到支付宝支付的入口。于是去淘宝让人代购= =

然后去godaddy那儿去设置使用dnspod解析dns，再去dnspod注册帐号再添加两个A记录指向github的ip就好了。等了几十分钟才生效。  
晚上换了套主题，又加上了多说系统（默认的那个不知为何没设置成功= =）。加了tag cloud（虽然不知道有什么用）。  
这些主题都有一定扩展性的，有能力的话可以在这些主题基础上修改或加入一些个人元素。  
熟悉之后也很容易对header, footer, asider做出改变的。  
像我就自定义了about me 和微博和tag cloud 等等～  

然后发现我对github那些还不熟啊= = 关于master, source那些。。。  
还有markdown语法，得补补基础先～

个人域名 plus 个人博客，有什么更爽的么 :D  
搞了一整天，终于基本搞定。  
**Hello Octopress !**  
看来真的是不折腾不进步哇哈哈 :P


