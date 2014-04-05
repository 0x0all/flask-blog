date:2014-04-05
tags:python,tornado,websocket,twitter
title:remote-project-from-Z
<!---->
#一道 python 远程笔试题  
看到某公司的官方招聘页面有“Web后端开发工程师”，于是三月就把简历投了一下，然后收到 HR 邮件，说先进行一下笔试考核，让我一周时间完成一个小 project 。题目其实就是做个 website ，用户在前端指定关键词，后端要把包含该关键词的 twitter 推文或微博内容 实时反馈给用户。  
<!--more-->
看到这题目其实马上想到的是 `node.js` 和 `socket.io` ，但我想用 Python 写，而且应该是 `tornado` 框架。于是去翻了那本忘得差不多了的 `Introduction to Tornado` ，这本书其实挺好的，除了少部分内容有点过时以外，比如它里面的 tornado 版本才 2 点几，还有里面用到的 `twitter search API` 现在也已经弃用了。于是我看了里面 `Asynchronous Web Services` 这一章，作者也是要实现一个实时的东西，先后用 `long polling` 和 `websocket` 实现。其实 `long polling` 看不大明白，好像直接让 `ajax` 定时请求？ 总之我看到了我要用的东西——`websocket` 。但书里那时候 `websocket` 还不是很成熟， tornado 里关于这个东西也还没定形。但我又去看最新的 3.2 的[文档](http://www.tornadoweb.org/en/stable/websocket.html?highlight=websocket#module-tornado.websocket)，现在已经基本定下来了，文档也很清晰。  
获取数据的话我选择 twitter ，因为它提供了 `stream API`，可以获取实时推文，渣浪扣得要死类似的接口一个都没有。但我又不想自己从最基本的授权开始去调用 twitter 的接口，所以想起之前用过的 [`twython`](https://github.com/ryanmcgrath/twython) ，看到[文档](https://twython.readthedocs.org/en/latest/usage/streaming_api.html)里果然有 `stream API` 的支持。 整个 project 实现起来不难，基本功能一天就写出来了。但其实还是有遇到一些问题。  
首先一个就是 `import` 路径问题，因为我想把 `Model` `Controller` `View` 分别作为一个 `directory` ，但 `Controller` 又需要用到一些 `Model` 里的类，试过一些相对路径的 `import` 都出错了，后来在 `__init__.py` 里把 `Model` 的路径加入 `system path` 才终于搞定。  
其次是 `twython` 的接口，获取实时推文嘛，开始运行之后就一直进入了 `on_success` 函数，实时推文就一直在这里出现。所以它是 block 的，整合 tornado 后点击前端 button 后端就一直 block 在这个函数里了。于是我也不知道怎么搞了，居然 google 到一个和我有一样问题的，他[使用了多线程解决](http://rjw57.github.io/blog/2013/06/24/geolocating_tweets_with_twython/)。老实说此前我几乎没有用 python 写过多线程和多进程的代码。但看他的 demo 和 `threading` 的文档也算搞起来了。于是再也不用阻塞在那个 `on_success`  接口了。但关于这个接口还有个问题，它（ Model ）获取到的推文无法返回给 Controller ，因为根本不是我调用的它。 但要返回给用户推文只能用 Controller 里面的 `websocket` 的 `write_message` 方法。所以我只能被迫把每个 `websocket` 对应的实例传到 Model 里再在 Model 里 write 给用户。这样代码其实很不好看，其次也违背了 `MVC` 的原则。。。  
这样写完我觉得差不多了，但测试多个用户时却出问题，A 打开网站并 monitor 一个关键词之后 B 也打开并开始 monitor ，这样子 A 的实时推文都会到 B 这边来 - - 应该又是那个 `on_success` 那里的问题，不知为何不同线程最后会共用一个 websocket 的 instance. 于是我想设置一个全局 session 字典， key 为 websocket 实例， value 为对应的 thread ，又是路径问题，一开始只是想让 M 和 V 和 C 分离开显得 project 清晰一点，到现在却成了坑，让一个东西全局共享就这么麻烦！ 后来我干脆把 session 做成一个类，这样 import 坑就比传变量少点，其次有一些针对 session 这个字典的操作，封装成一个类其实也很不错。  
最后前端我直接用了  jQuery 和 [`Topcoat`](http://topcoat.io) 这个 CSS 框架，因为自己调整每个细节实在太痛苦了， Topcoat 还挺整洁漂亮的，有空把博客的前端也重构一下。  
过了几天走在路上就接到 HR 的电话，安排时间进行电面。哎码写了几天的 project 还是得到了肯定，我觉得主要原因是我实现了功能；在自己 VPS 上部署了 demo 供访问；还算不错的注释以及几乎完全的 `PEP8` 规范。  
最终效果：  
![demo](http://bcs.duapp.com/wxtuku/PcSt5YjJ5l.png)  
全部代码可在 [Github](https://github.com/yakiang/real-time_tweets) 得到。  
电面经历的话请看[下篇](/blog/remote-interviews-from-Z)
