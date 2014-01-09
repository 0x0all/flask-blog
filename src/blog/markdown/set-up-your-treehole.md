date:2013-06-28
tags:weixin,renren,python,sae
title:set-up-your-treehole
<!---->
#[微信-人人]树洞教程
寒假时给自己学校建了个微信-微博的树洞，之后陆续收到有人请教我怎么做的邮件，而且还是微信-人人的。由于没接触过人人开发所以也没帮忙。后来偶然去看了下人人API神马的，用python很快就写了个能发布状态的脚本。后来公布自己邮箱后越来越多人联系我问我怎么搞，在帮三个大学搭起人人树洞后我们也进入考试周- - 今天考完了，还是来把教程简单写一遍，有需自取，免得我一个一个去说怎么做。。  
转载请注明本文链接！微信-微博树洞教程在[这里](/blog/set-up-your-weibo-treehole/)  
说明：本教程的树洞基于SAE平台，使用Python实现（不会编程也不影响）。在开始之前，你应该有一个人人的公共主页；然后去[SAE](http://sae.sina.com.cn) 注册一个SAE帐号(而且要尽快通过手机复验、实名认证），还要去[微信公众平台](http://mp.weixin.qq.com) 注册一个微信公众帐号并通过审核。这些自己搞定，就不细说了。  
<!--more-->
首先，打开[这个网页](http://sae.sina.com.cn/?m=myapp&a=create)填写并创建应用信息：二级域名可以随便写，比如你的大学拼音，不过不能和别人重复；应用名称同样随便写；开发语言记得选python；应用类型默认就好。  
创建之后，在顶端右边“我的应用”那里，进入你刚刚创建的应用的页面。然后在左边一栏里选择“代码管理”，  
![](http://img2.tuchuang.org/uploads/2014/01/sae1.png)  
这时候是没有代码在上面的，点击“创建一个版本”，默认名称为1就好。  
然后点击“编辑代码”（可能需要输入密码，输入密码后可能还需要点多一次），然后就进入了在线代码编辑的地方。这时候直接把左边那两个文件都右键->删除掉（如果config.yaml删不掉就点开它然后把内容都删了，把我那份的内容复制进去就好）。然后点击上传（黄色箭头），把我这里[两个文件](files/th-codes.rar)解压后分别上传上去。  
上传完后，双击左边的index.wsgi这个文件进入编辑模式，在第30行处的单引号内填上你的人人公共主页的id，这个id哪里来呢？你只要打开自己的人人主页应该就能看到了，就在网址上，比如  
![](http://img5.picbed.org/uploads/2014/01/page_id.png)  
你只要把你自己的人人公共主页的最后那一串数字复制后填到代码30行的单引号内就好了。然后点击右上角的全部保存。   
然后，进入[人人开发平台](http://app.renren.com/developers/baseinfo)，先完善基本资料，再到[这里](http://app.renren.com/developers/createAppV3/create)创建一个新应用。应用名称、分类都随便写，根域名就写你刚刚创建的SAE应用的域名（比如whatever.sinaapp.com），应用图标随便找张图调整成4种像素的大小然后上传吧。创建成功后就能得到这个应用的APPKEY、Secret Key等信息：(现在APPKEY已经改名为APIKEY，所以如果你看到的是APIKEY，其实是同一个东西）  
![](http://img3.tuchuang.org/uploads/2014/01/appinfo.png)  
先把APP KEY的值复制后填到刚刚的代码的51行处的单引号内，把Secret Key的值复制后填到代码52行单引号内。点击保存。  
然后，点击“应用信息”，在右边选择添加“网站连接”，网址还是写你的SAE应用的地址，比如http://whatever.sinaapp.com ，记得别少了http:// 。然后点击保存！！__不要审核__！！  
然后打开`https://graph.renren.com/oauth/authorize?client_id=【1】&redirect_uri=http://【2】.sinaapp.com&response_type=code&scope=status_update+photo_upload+admin_page`
其中要把【1】替换成你刚刚得到的APP KEY，把【2】替换成你的SAE应用的名称。替换后在浏览器打开这个地址就好了。他会让你授权，授权后跳转到你的SAE应用的页面，应该会出现“没有部署代码”或者“internal server error”之类的错误但不用管它，我们要的只是这个页面上面的网址而已：  
![](http://img3.tuchuang.org/uploads/2014/01/getcode.png)  
把你跳转后的网址的"code="后面的那串字符复制后先保管好。然后打开`https://graph.renren.com/oauth/token?grant_type=authorization_code&client_id=【1】&redirect_uri=http://【2】.sinaapp.com&client_secret=【3】&code=【4】`
其中【1】和【2】还是按刚刚那样替换，再把【3】替换成刚刚注册人人应用后和APPKEY同时获得的Secret Key，把【4】替换成刚刚让你保管好的字符串。替换后再在浏览器打开这个地址。然后就会在页面上出现长长的东西。找到refresh_token和access_token：  
![](http://img3.tuchuang.org/uploads/2014/01/rtoken.png)  
![](http://img5.tuchuang.org/uploads/2014/01/atoken.png)  
把refresh_token的值复制后（注意复制完整，是第二个双引号内的所有内容）填入代码77行的单引号内（如果提示会话超时就需要刷新后重新填，所以之前的保存很重要）。同样地，把access_token的值复制后填入代码78行的单引号内。点击保存。  
到这里代码就搞定了。  
打开[微信公众平台](http://mp.weixin.qq.com)，进入“高级功能”，点击“开发模式”，然后填写接口配置信息，URL还是写你的SAE应用地址（比如http://whatever.sinaapp.com ），Token则随便写都行。然后提交，如果回复你绿色的消息就代表成功了。如果没成功肯定是中间哪里出错了，可再仔细校对下代码。（注意那个"code"不能重复使用）  
如果提交成功的话，现在就不论你发送什么到那个微信公众帐号，它都会把你的消息发送到指定的人人公共主页了。  
这样，微信-人人树洞就算搭建成功了～！  
有任何问题都可以评论或者发邮件给我。如果你成功了也希望你能在评论下面留下你的学校 ^ ^  
PS: 目前成功的大学有：  
燕山大学， 渤海大学， 天津医科大学，重庆大学，安徽医科大学，北京工业大学，上海应用技术学院，  
<br><br>
2013-10-13 更新：  
如果你不想折腾又想建树洞，而且愿意付费，欢迎私聊我 --- QQ 六七四六九一九三五  
