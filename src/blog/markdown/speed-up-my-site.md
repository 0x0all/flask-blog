date:2014-02-13
tags:web,cache,crontab,server,vps
title:speed-up-my-site
<!---->
#一次网站优化经历
在 V2EX 看到有人分享了 99￥/year 、1G 内存的 vps ，身为穷逼一时心动就入了。当晚 ping 值平均200ms，比起这个 blog 已经快了，觉得真赚了，一下子就把平时习惯的配置都在上面部署了一趟。不得不说很享受配置一个全新 Linux 的感觉，不过考虑到以后越来越多这种情况，应该设法把它搞成自动化的。  
结果第二天 ssh 过去超慢，再 ping 一下居然 500 多……然后从那到现在 ping 值都有至少三四百的水准 orz 。但还是得用啊，于是把之前给高中弄得微博树洞（以下简称 nest ）迁移过去。nest 之前是放在 SAE 的，由于访问量不高也不怎么吃云豆 =。= 但由于要小规模重构，决定把它迁出来到 vps 上，毕竟 paas 自由度有点低。  
<!--more-->
重构好了，也部署上去了（依然是 `flask` + `uwsgi` + `nginx` + `supervisor` ），但发现速度慢的问题挺严重的。因为 GET nest 的首页的话，后台首先会 GET 微博的 API ，获得 20 条最新微博，由 `jinja2` 合并成一页再 render 出来。机房在 LA ，这个过程花了差不多四五秒……以前放 SAE 这个过程还是挺快的，虽然比较耗云豆但也没想过整改，现在我想把它当作一个真正的网站来优化，于是就研究 speed up 的方法。  
###方案一
机房速度慢这个改变不了，于是可以想办法不去 GET 微博的数据，如果用户来访问时马上把 html css js 都给它，速度肯定快了不少。所以我使用了 `crontab` ，一直觉得这个东西让很多需要严格时间管理的事务变得很方便。我在 flask 加了一个路径（假设 `/abc`），功能和上面提到的首页一样，先访问微博 API 再 render。然后让 crontab 每分钟都去` curl` 这个 `/abc` ，得到的结果保存为一个页面（假设叫 `ready.html`）。

    */1 * * * * root  curl http://127.0.0.1/abc > /path/to/ready.html

然后用户访问网站首页时再把这个 `ready.html` render 出去。如此一来用户就不用等待访问微博 API 的过程了，如果同一时刻有多个人访问压力也不会那么大，对用户对 cpu 都是一件好事。只不过微博内容不会那么实时而已，不过一分钟的缓存应该算不了什么。
###方案二
但第二天又觉得不大好，毕竟 nest 只在周末有点访问量，平时以及半夜每分钟访问一次微博的 API 大部分最后都没用上，白白去掉了流量。如果可以这样：在一分钟内，来访问的第一个用户需要等待几秒，相当于访问 `/abc` 一次，然后后台把最终的 html 保存下来（还是叫 `ready.html` ），在这一分钟内如果还有用户访问就把 `ready.html` 给他，时间过了就把它删了，下一分钟还有用户来就再重复这个过程。  
于是我是这么处理的：

    try:
        return render_template('ready.html')
    except Exception as e:
        get_weibo_statuses()
        return render_template('ready.html')

用户访问时先试着把 html 给它，如果文件不存在，抛出了异常，在 `get_weibo_statuses` 方法里就去 GET 微博的 API ，然后把得到的数据处理后写进 `ready.html` 。  
最后在 `crontab` 是这么写的：

    */1 * * * * root  rm -f /path/to/ready.html

每分钟定时删掉这个 html 。  
这样平时没用户访问时后台也不会白白每分钟去获取最新微博浪费流量了。搞定时个人觉得还是挺赞的，虽然 `get_weibo_statuses` 方法里的代码实在太难看了。。。
###方案三
很快又发现方案二行不通了，网站访问量本来就不高，同一分钟有多人访问的情况更少。即使一天有来十几个人很大可能也是在各自时间点来的，也就是说这些人都要花几秒等待页面，而后台保存的页面在一分钟内就被删了…与最初加速网站的初衷反倒越走越远了。  
其实要不要去 GET 最新的微博根本上取决于微博有没有更新，于是我在想如果能像 js 的 event-driven 那样，微博数有变化就通知服务器，我再去 GET `/abc` 保存为 `ready.html`，这样既省流量和 cpu ，所有用户也都不用等待太久。  
但我知道这不大可能。于是只能自己定时去查看微博数有没有变化了。一开始找到了[念知](http://nianzhi.cc)这个站，就用 crontab 每分钟去 GET 里面的指定用户，再解析得到微博数。当然本地数据库也要保存一份最新的微博数，如果两个数目不相同，就更新一下 `ready.html` 的内容，然后更新本地数据；相同的话就什么都不做。  
但很快发现念知的数据不是实时的，发了新微博后十分钟，它的数据都是不变的。这也很正常其实，毕竟是第三方的。如果直接去找 http://s.weibo.com 很快就又会需要验证码，吃过它的苦了。而直接 GET http://weibo.com/u/xxxxxx 就会有 `cookie` 问题要处理。找来找去都没有实时的好站点。于是只能自己做了。  
我想到了 BAE ，之前玩过一阵，和 SAE 差不多，不过除了 SVN 外还支持 Git ，而且每天有一定量免费限额。于是在上面简单部署了个 `web.py` ，把微博的 `uid` 作为参数发给它，它就会返回该用户的微博数。 
![duapp](http://img5.tuchuang.org/uploads/2014/02/1432432.png)  
所以就 crontab 就变成了每分钟 GET 这个指定的 url 。不知道 BAE 的具体免费限额多少，但一天这么下来也没出问题，应该是页面也确实是只有简单的几个字符的原因吧。  
就这样，虽然比理想的 `event-driven` 差点，但也不错，目前就是这样做到 user-friendly, bandwidth-friendly, cpu-friendly 。唯一不爽的应该只有 BAE 了 LOL 。  

---
其实加快网站访问方法很多，yahoo 的这篇 [Best Practices For Speeding Up Your Web Site](http://developer.yahoo.com/performance/rules.html) 罗列了不少，比如 `CDN` ，使用 `gzip` 压缩， 做好缓存，压缩 css/scripts ，放好 css/scritps 的位置，重定向时使用 3XX response code 而不是用 `<meta>` 标签或用 js ，等等。  
其他的还没有研究，不过我对缓存倒是很有兴趣。在 heroku 的这篇 [Increasing Application Performance with HTTP Cache Headers](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers) 就详细介绍了在 http header 可以怎么设置缓存。文章还是很好的，只是我弄懂了大致的那些概念后却不知道怎么实现了，比如一个 html 文件里有几个 css 、js 、 image 文件，每个文件都有想设置的 `cache header` ，我应该怎么做，在 flask 设置（好像做不到）还是 Nginx ？ 文件多的话一个个写好像不大科学，没有更好的做法吗？但是搜来搜去好像都没找到相关的 tutorial …… 过几天去找个人多的 forum 问一下好了。 

---

我觉得以后做 backend developer 其实挺好的，关键是这是自己喜欢做的事。本来这学期开始可以去做相关实习了的，搞到最后还是去不成，而且接下来一段时间可能都做不了了。最近实在很迷茫，前途未卜 =。=  唉 


