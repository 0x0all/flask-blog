date:2013-04-21
tags:python,baidu
title:tieba-autosign-with-python
<!---->
#Python实现的贴吧签到
2013-6-1 更新：  
本代码已失效，但原理不变。有意者可以弄明白后自己试一下～  
<br>
<br>
自从从别人博客那里学会了python登录微博和人人后，身为一个python爱好者遇到什么网站都想用python来实现登录。
比如登录过我们学校的教务系统，还有飞信网页版等等。  
而写一个脚本来实现贴吧签到的想法是早就有了的。之前也写过一个，但当时以为失败了，便没再弄。  
今天重头开始写，成功后才发现原来之前写过的那个也是登录成功的 = =   

我选的是[贴吧wap版](http://wapp.baidu.com)，这样登录起来会少很多麻烦（比如可能会有随机码和密码加密等）。  
先用火狐的httpfox (或者firefug之类的也行)检测登录贴吧的过程中和服务器的http交互数据。  
<!--more-->
![httpfox](http://img3.picbed.org/uploads/2014/01/tieba_autosign.png)  
一般分析postdata时如果有类似随机码或加密数据之类的那我一般是没法实现模拟登录= = 有时会重复登录或者切换马甲再登录观察一次，
如果那些莫名其妙的数据没变或者有规律可循那是最好的了。否则我的话就只有放弃了。  
这里还好，大多数数据都很简洁，只有一个uid有点费事，但通过切换马甲登录我发现这个数据好像是不变的。于是我就直接使用这串数据来模拟登录了。   

然后签到也类似，通过httpfox观察到签到这个过程实际上只是GET了一个地址而已。(如果不是wap版贴吧就没有这么容易了。)  
但是get的这个地址里面包含了tbs和fid这两个参数。一开始我又以为是固定的，后来发现不行。
再仔细检查发现就在要签到的贴吧的页面源码里。  

直接在代码里解释好了：


    #!/usr/bin/python
    #-*- coding:utf-8 -*-
    
    #登录--> 获取ssid --> 进入某一贴吧 --> 获取tbs & fid --> 签到
    
    import urllib
    import urllib2
    import cookielib
    import time
    
    # 以下几句实现了保存cookie功能，是为了登录后能成功签到。
    # 原理其实我还不大明白，是从别的大牛来的。
    cj = cookielib.LWPCookieJar()  
    cookie_support = urllib2.HTTPCookieProcessor(cj) 
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)  
    urllib2.install_opener(opener)
    
    # 登录
    username = raw_input('请输入登录的用户名: ')
    passwd = raw_input('请输入密码: ')
    uid = '936D8C303C6F8F6A25F1F6B8D8353B69'
    # 下面是httpfox来的数据
    loginurl = 'http://wappass.baidu.com/passport/'
    logindata = {
            'login_username':username,
            'login_loginpass':passwd,
            'aaa':'登录',
            'login':'yes',
            'can_input':'0',
            'u':'http://wapp.baidu.com',
            'login_start_time':int(time.time()),
            'tpl':'tb',
            'tn':'bdIndex',
            'pu':'',
            'ssid':'',
            'from':'',    
            'bd_page_type':'1',
            'uid':uid,
            'login_username_input':'0',
            'type':''    
            }
    logindata = urllib.urlencode(logindata)
    
    req = urllib2.Request(url = loginurl, data = logindata)
    login = urllib2.urlopen(req).read()
    if '密码有误' in login:
    	print '密码错误，登录失败'
    	exit(-1)
    
    # 登录成功后的数据里有一个地址，里面有接下来要用到的ssid。
    # 不过我是用处理字符串的方式来提取ssid，略低效和笨拙
    p_ssid = login.find('ssid') + 5
    login = login[p_ssid:]
    p_ssid_2 = login.find('"')
    ssid = login[:p_ssid_2]
    
    # 签到
    ba = raw_input('输入贴吧名字:')	
    ba = ba.decode('utf-8').encode('gbk')
    # 要先模拟打开这个贴吧，在打开页面的html里获取下面要用的tbs & fid
    temp_qdurl = 'http://wapp.baidu.com/mo/q-%s--%s--1-1-0--2/m?kw=%s' % (ssid, uid, ba)
    html = urllib2.urlopen(temp_qdurl).read()
    if '尚未建立' in html:
    	print '贴吧不存在'
    	exit(-1)
    
    # 同样笨拙的方法来提取tbs & fid
    p_tbs = html.find('tbs')
    tbs = html[p_tbs+4:]
    p_tbs_2 = tbs.find('&')
    tbs = tbs[:p_tbs_2]
    
    p_fid = html.find('fid')
    fid = html[p_fid+4:]
    p_fid_2 = fid.find('&')
    fid = fid[:p_fid_2]
    
    qd_url = 'http://wapp.baidu.com/mo/q-%s--%s--1-1-0--2/sign?tbs=%s&fid=%s&kw=%s'%(ssid, uid, tbs, fid, ba)
    qiandao = urllib2.urlopen(qd_url).read()
    
这样就搞定了。其实有不少改进空间的，比如可以实现从一个文件中读取所有贴吧列表逐一签到，还可以用PyQt实现一个GUI版，
还有应该加入更多异常处理，或者把一些操作封装在函数里等等。  
  
__Python__ 实在是很简单又很强大很全能的语言！  
  
   

4-24 更新  
做成了exe文件，可以批量签到。[下载](/static/files/tieba.zip)  
  
  
  

6-1 更新   
貌似这个代码失效了，原因可能是上面的uid有变，得重新用httpfox看一下修改一下才能用估计。。  
太懒了暂时先不搞了 -。-   


---
转载请注明出处，谢谢!
    
