date:2013-09-30
tags:,weibo,twitter,python
title:weibo-rtkcn
<!---->
#微博版中文锐推客
作为程序员哪能不翻墙，翻墙哪能不上推。偶然看到twitter上[@RTKcn](https://twitter.com/RTKcn) （昵称是“中文锐推客”）这个帐号，觉得很不错，它会自动获取twitter上转发最多的中文推再转推到自己帐号，介绍页面在[这里](http://rtbot.laobubu.net) 。  
然后它的推文质量确实挺高的，就不说那些不适宜在天朝出现的了，其他的大都很搞笑，而且目测微博上一些很火的段子原始出处也是twitter来的。然后我就曾想把它一些好的推文发到自己微博帐号上，于是曾经琢磨着写个Chrome插件，可以在twitter页面直接发到微博上去。暑假时钻研了许久，最后还是失败了。Sigh，插入自定义`css`和`js`到头部了但就是不按我要的方式来；`post`到一个页面里已有的隐藏`iframe`了（而且它本身发推的表单也是target到这个iframe）但就是post完要重定向。无奈作罢。。。  
等到前两天才想起可以做一个微博上的锐推客，把twitter那个的推文照搬过来就好了，反正vps在美国上推不成问题，`ping weibo`也不慢。想到就干，申请了微博帐号[@中文锐推客](http://weibo.com/RTKCN) 后（lucky，没人叫这名字)，就去研究twitter开放平台文档了。  
<!--more-->
由于有过新浪微博，人人，网易微博等等的Oauth开发经验，本以为Twitter也不难搞定，太天真了。一进去看到那么多文档有点懵，又是`Oauth1`又是`Oauth1.1`又是`Steam Api`又是`REST Api`的，不知道区别和哪个是我要的。后来在REST首页看到我要的接口 [get/statuses/user_timeline](https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline) ，我要的只是获取 @RTKcn 的推文而已，所以这一个接口就够了，其他的就不去看了。  
然后是申请应用，申请完是很折腾的一个钟。一开始我直接访问`https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=RTKcn`，215错误，看来要授权。然后研究怎么获取`Token`，后来发现在应用页面就可以直接获取了。然后自己写个Python脚本，还是访问上面这个页面，但是在`headers`里加入了token等信息。结果还是`400 Bad Request`，有点不知道怎么搞了。Google之，才发现[Twitter](https://dev.twitter.com/docs/twitter-libraries) 上自己就推荐了很多SDK，而且Python类的SDK很多，于是接下来很长时间我在尝试各种sdk，都是先访问`Github`主页看`README`，感觉不过时再按它的教程来搞。先后安装并尝试了`python-twitter`,`tweepy`,`TwitterAPI`等几个SDK，但都有这样那样的问题，它们不是在授权时有问题，就是在`status_update`也就是发新推文时出错。最后一个尝试了`Twython`，同样发推有问题。那时好烦就去洗澡了，洗完继续搞时忘了在哪里看到Application有`只读`和`可写`的区别。我这才想起来自己应用上面写的`Read-only`是什么意思。它的只读决定了它只能`GET`，不能`POST`，大概就是这么个意思。所以发推会失败，但没关系。我只是要`GET`推文而已。  
![Read-only Application]({{ root_url }}/images/articles/readonly-application.png)  
于是继续使用`Twython`这个sdk，`GET @RTKcn` 的推文果然成功了！至此`twitter`端基本搞定，剩下的只是分析下`json`获取推文内容了。  
  
至于微博那边就很简单了，自己已经写过好几个这种使用`未通过审核应用`发微博的机器人了 :P 。  
  
后来发现`twitter` 的`json`也没那么容易搞定，因为twitter的`RT`机制我一直搞不明白，更不清楚它返回的`json`内容都代表什么意思了-。- 还有图片`url`的获取，第一次正式在python中使用正则来匹配。试发一条时发现新浪返回`含有不合法Url`错误，调试后发现是`http://t.co/xxxx`这个，好像是twitter的短链接来着。于是又用正则匹配把这样的url都替换掉了，不过应有的链接还是有的。  
  
代码基本搞定，就让它每分钟在服务器运行一次就好了。之前有搞过`crontab`这个文件，大概了解怎么写吧。于是我就加上  
`* * * * * root python -B /path/to/the/project.py`  
可是每分钟过去了什么都不发（@RTKcn 是有新推文的），当时实在很纳闷。因为自己运行`python RTKcn.py`明明是可以发的。折腾了好久，终于搜到[这个](http://163.fm/5CP2mqh) 和[这篇](http://163.fm/Py3yNf3)，里面都提到了一个问题：Python脚本里使用本地文件时必须使用绝对路径，shell 命令也是！  
当时就mlgb了，赶紧改。顺便把脚本`chmod +x`改成可执行的，`crontab`改成这样：  
`* * * * * root /path/to/the/project.py`     
然后就好了！放到[github](https://github.com/yakiang/weibo-RTKcn)后就收工了。  
大家可以关注一下这个微博，保证内容不会让你失望的 ：P  
<br>  
--- 

13-10-12更新：  
才十几天，今天这个号就因为太多不和谐内容就给渣浪封了 T_T ，懒得去申诉了，唉。  
