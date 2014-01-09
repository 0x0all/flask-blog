date:2013-09-11
tags:vim,python,vps,ssh,web,shell
title:notes-of-summer
<!---->
#Notes of Summer
两个月的暑假过了，终于开始大三鸟-。-  
暑假时买了个低配置VPS当作自己的生日礼物，后来又系统地学学前端，主要是js，积累了些笔记，就一次性记在这里吧。  
<br>
首先是编译vim7.4 。由于官方还一直是7.3，为了[YouCompleteMe](https://github.com/Valloric/YouCompleteMe)所以干脆升到7.4好了。  
由于某种狗日的原因vim官网上不去，所以我去了[这里](http://ftp.tw.vim.org/pub/vim/unix/)下载最新代码包。  
<!--more-->
解压，然后安装需要的编译依赖工具：

    sudo apt-get install build-essential xorg-dev libx11-dev libgtk2.0-dev libncurses5-dev python-dev

然后进入刚刚的文件夹，运行以下命令看依赖项是否解决，有问题再安装指定包。要注意的是不能一句`./configure`这么简单，否则编译安装完的vim无法支持Python和Ruby。  

    ./configure --disable-nls --enable-multibyte --with-tlib=ncurses --enable-pythoninterp --enable-rubyinterp --with-features=huge

然后就是`sudo make`和`sudo make install`了。  
<br>
然后ssh连接vps时可以通过`~.`来断开无响应连接。参考：http://www.vpsee.com/2013/08/how-to-kill-an-unresponsive-ssh-connection/  
我相信它是有用的，但不知道为什么我就是经常用了也不断开=。=  
  
然后如果ssh刚登录时出现 `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!` ，可以通过在自己电脑 `mv /root/.ssh/known_hosts /tmp` 解决：http://hi.baidu.com/meloidea/item/7d0775ea0fdbf5f6e0a5d4b4#713670-t163-1-17044-cde5936298d1595ae559c6ce9193b1af  
<br>
然后一开始在vps配置nginx+uwsgi+python时老是出现各种502问题，日志里一般是` unavailable modifier requested: 0 `或`upstream prematurely closed connection while reading response header from upstream `, google了一上午还是在官方文档解决。在uwsgi配置文件加入`plugin, chmod-socket, chown-socket`才解决：

    chmod-socket = 666
    chown-socket = www-data
    plugin = python

前两个跟权限有关系。之前我曾经通过修改`nginx.conf`的user为`root`解决但不安全而且不是长久之际-。-  
<br>
然后想让机器开机自运行某句自定义命令可以将命令加进`etc/rc.local`最后一行的 `exit 0` 前面。再在命令行运行 `chmod +x /etc/rc.local`让它具有可执行权限。再重启就ok了。  
<br>
然后遇到一个奇葩问题，无法在html里import `static`里的`css/js`文件（web.py），在本地和SAE都不会有这种问题。而且搞了很久很久都不行，都去`stackOverflow`提问了，结果想到可能和uwsgi有关，因为本地的可以是因为没用到uwsgi。然后google `uwsgi path`果然解决了：http://uwsgi-docs.readthedocs.org/en/latest/Options.html 。同样在配置文件加入这句：

    check-static = path/to/your/source/code

<br>
在`PearOS`安装过程中最好不要勾选“不需密码自动登录”，我就是这样的结果安装完就一直卡住了进不去。重新安装时不勾选就没事-。-  
然后在64位系统上用`gdebi`安装一些只能在32位系统运行的软件包时（比如WPS）最好先乖乖安装`ia32-libs`，像我那次就是没有先安装，结果好像WPS把我机器当成了一个“安装了很多64位软件的32位系统”，然后开始一个一个卸载掉。。。。。我了个去，其实它是有提示的，“要卸载xxx个软件包，是否继续？”（200个以上），我没反应过来就按了回车，到了一半看到它一直在卸载才反应过来。。。已经来不及了，重装一次= =  
<br>
如果SSH连接响应太慢，可以尝试在服务器上`/etc/ssh/sshd_config`文件中修改或加入`UseDNS=no`  
搭建ftp实在不是一件轻松的事，建议使用`proftpd`   
如果在有些机器的终端上发现按`Tab`键不会补全，或者按方向键没有出现上/下一条命令而是一些奇怪的字符，很可能你在用的不是`bash`，而是`sh`，只要修改用户默认登录shell就可以了：

    chsh -s /bin/bash

<br>
如果一个网站有分PC版和wap版，在根据UA判断时应该在服务器后台来判断。比如用`web.py`时获取UA：`web.ctx.env['HTTP_USER_AGENT']`，再使用 `raise web.seeother()` 来引导。而不要在前端使用js来判断和重定向。这样既耗用户流量，而且js判断和重定向效果不好，比如奇葩浏览器`UC web`版，能判断，但重定向经常失败。  
<br>
使用`YouCompleteMe`时，有时打开一个`python`文件会输出`Error importing jedi. Make sure the jedi submodule has been checked out. `，其实`jedi`只是一个用于补全的插件而已，一句`sudo pip install jedi`就好了。  
<br>
要在python脚本运行`shell`命令时，一般可以`os.system(cmd)`，但这样没法获取结果的输出内容，所以可以这样：

    import os
    result = os.popen(cmd).read()

<br>
一般终端下`ls`出来的文件夹都是深蓝色的，如果终端是黑色的那简直是受罪，多亏google到[这篇](http://www.bigsoft.co.uk/blog/index.php/2008/04/11/configuring-ls_colors)文章, 在`home`下面创建一个`.dir_colors`文件，把下面两句加进去就可以了：

    LS_COLORS="di=01;93"
    export LS_COLORS

<br>
今天入了个背光键盘，作为夜猫我居然忍了两年。。以后方便多啦～！  
<img src='http://img5.tuchuang.org/uploads/2014/01/beiguangkb.JPG' width='700px;'>  
但在linux下无法按指定键toggle灯光，最终在[这里](http://nyc1991.blog.51cto.com/6424159/1162345#559183-t163-1-74302-bfd8773de2eba945e7c660a538292c40)找到解决方法。  
简单来说，在终端敲下面两句就可以了。

    xset led  named 'Scroll Lock'  # 开灯
    xset -led  named 'Scroll Lock'  # 关灯

<br><br>
###小结
之所以买低端vps目的就是进一步学习搭建服务器和学习linux，目前看来还是有效果的。其实不断google最终找到解决方法是一种享受来的。。  
要建站以后估计要狠下心买`linode`或者`digitalocean`了啊。。。穷逼学生啊 T_T  
    
    
  


