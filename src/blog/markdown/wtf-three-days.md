date:2013-08-08
tags:linux,octopress,blog
title:wtf-three-days
<!---->
#折腾的三天,真苦逼
###<a id='linux'>系统篇</a>
5号晚上忽然发现Mint上不了网了，NetworkManager 那里不知为何没有了无线这个选项。此前mint一直是很好用的，但我没去怀疑硬件问题。以为是系统坏了，重启无效后心想难道是上天都要我换系统了吗。
因为我垂涎Fedora和Arch很久了。但mint一直用得很顺手，虽然是个开箱即用的适合小白的系统，但我本来就不是什么大牛，系统嘛还是用得顺就好。所以一直没换。更何况系统的mysql里有一个爬了挺久的数据库，当初脑袋发热想统计下全国高校每个手机发微博的人都是用得什么系统。就建了个python项目，用微博api去取用户和用户发的微博尾巴，自己写爬虫去抓每个用户的大学（这个api已经不支持了只能自己抓）。然后自己抓其实是很没效率的，微博的cookie一天就失效，而且每个用户的大学居然能花几秒来抓。。其实我该优化下的但迟迟没动手。结果是没有服务器的情况下，想起这个项目时就顺便运行一下，所以每天抓的时间很少，几个月下来才5万多用户+一万多有具体数据（大学、手机客户端类型）的用户。由于换系统还得备份mysql，所以一直以来都在使用mint。  
<!--more-->
但现在无线都没了还玩毛啊，只能重装一个了。要重装肯定不会再选择mint。那天中午其实我在另一台电脑安装了kali，发现有很多安全方面的工具，但不适合当平时使用的系统。于是决定再试一次Fedora。此前我已经尝试不下二十次安装Fedora，无一成功。原因各种，可能是UEFI的问题，也有其他的，有时候根本刻录完iso都进不去live环境，有时候终于进入了安装时却遇到bootloader的问题。总之就是没成功，可是越得不到越想要，所以一直都想试试Fedora。因为从Ubuntu到Kubuntu到mint，一直在debian系都腻了。。  
![kali](http://img2.picbed.org/uploads/2014/01/kali.jpg)  
这次用dd命令刻 iso

    su -c 'dd if=Fedora19.iso of=dev/yourusb'

然后不用改什么东西就顺利进了live环境，还是很出乎意料的 - - 然后是分区之类的细节（装系统无数后已经大概明白原理，不像新手那样怕设置错误然后数据全丢了）。虽然在回收空间那里卡了一会，但很快还是开始安装了。我之前那么多次尝试，真正能够进入安装界面的情况才两三次！顿时内牛，鸡冻不已。而且最后没有报错就安装成功了，着实惊喜，还晒到了Instagram上。Fedora社区很赞，在官网下系统不论你在哪速度都不会慢，会根据你ip选择最适合的源给你，在学校时最多试过几M每秒。而且系统汉化也做得很好，很多系统的安装界面都提供很多语言，但像mint最后安装完成了大部分语言还是英文的，而fedora则汉化得很彻底。  
![fedora](http://img2.picbed.org/uploads/2014/01/fedora.jpg)  
装好系统以为终于可以体验rh系时发现这边同样没有无线！开始怀疑是网卡问题了于是切回windows看，果然那边也没有！无线网卡坏了么？可是什么也没动怎么也能坏。。Mint我真是错怪你了 T_T 。。然后我才想起一个重要事实：安装fedora之前在备份各种文件时，什么都考虑到了（包括各种配置文件），却单单落下了很重要那个数据库！！我辛辛苦苦爬的啊T_T，就这么没了。。。  
然后我不知怎么办了= = 如果是无线坏了自己也不会修，只有找联想服务站了。官网看到最近的服务站都有一百公里，我差点都打算自己拆机看看了。结果重启几次后奇葩得好了= = 自己就连上了wifi，所以这是怎么回事= = （事实证明重启就和心情不好睡一觉一样有效）。。  
然后开始配置fedora了，首先肯定安装git和vim，再把vim配置git下来，多亏了vundle，一切都很简单。但我发现fedora的X容易卡死，画面一动不动，只能强制关机，一天就卡了两三次（后来发现可能跟我关闭了独显有关）！而且配置monaco字体失败，这是很好看很适合coding的字体，没有这字体完全没动力了好么。我先忍了，再发现安装rvm也出错，具体原因忘记了。也就是说装不上ruby，也就是说配置不了octopress。。。综上，玩不下去了。。  
看来还是不习惯redhat系，于是又去下载debian。之前玩的都是基于debian的，这次干脆直接使用debian好了。安装基本组件就用了好久。。然后还问我要不要装图形界面= = 终于安装完成，进去后居然全都是乱码，给跪。任何中文都显示为方格，我tm想设置语言都不知道怎么搞。最后在[这里](http://mtoou.info/debian-zhongwenxianshi/)找到解决方法：去网上下一个simsun.ttf，放到`/usr/share/fonts/truetype/`下面，再运行`dpkg-reconfigure locales` 设置为zh_CN.UTF-8就好了。然后发现debian同样没有无线选项！以为又坏了，去windows一看wifi可以啊，再回来debian还是没有。google才知道不预装无线驱动！给debian跪。。于是去找驱动，然后去终端才发现sudo都会出错，一搜才知道连sudo都要自己安装！长跪不起。。`apt-get install sudo`。。。这debian也太tm 陋了。最后解决无线的方法是（debian7为例）：

    deb http://ftp.cn.debian.org/debian wheezy main contrib non-free # 把这句添加到/etc/apt/sources.list中
    sudo apt-get update
    sudo apt-get install firmware-iwlwifi
    
重启就好了。然后再次发现monaco安装出错，chrome安装有依赖，只能装chromium，而chromium不自带flash插件，自己安装也出错，连其他系统都有带的高级设置还得自己安装tweak tools才能进去设置。加上一开始中文、sudo、无线驱动各种缺，以后还不知道缺少什么东西。心想既然都是debian系，我干嘛要用这么简陋的debian，原来的mint不是一直用得很顺吗。好吧，于是刻录了mint15。  
折腾两三天的结果就是把mint14升级到mint15。。。mint安装是几个系统中最快的（不过fedora关机超快），装完首先去搞monaco，意外也出错，导致中文看起来也是方块，修改了很多次重启了很多次都不行。觉得这是我自己搞出错，于是重装mint，这次去[github](https://github.com/todylu/monaco.ttf)找一个monaco improve版，然后就好了，中文也正常。熟悉的系统终于又回来了。其实mint真的很不错。gnome在其他系统都不好看，包括debian，kali，fedora。别看fedora好像挺炫的，打开文件夹我觉得顶端栏好难看。。mint则不会，而且安装软件的话fedora和debian都很难看，mint自带那个相对来说还要可视化一点。最重要的是，能用monaco才是王道:D  
![mint](http://img3.tuchuang.org/uploads/2014/01/mint.jpg)  
  
###<a id='octopress'>Octopress篇</a>
在恢复Octopress前我还装了zsh，很方便的工具，就是启动有点慢。然后安装rvm和ruby，在`rvm install ruby-1.9.3`时卡住了，一直说 using Zsh 无法显示进程，be patient...然后过了很久都不行。结果换到bash就好了。然后我发现按照自己之前恢复octopress的博文自己都会搞错- - 索性再次删了repo重建一遍。这次把octopress和github之间的关系弄更懂了一些。还是从头简单写下吧,在debian系下有效。  
搭建Octopress：

    sudo apt-get install git curl
    curl -L get.rvm.io | bash -s stable  # 安装rvm
    source ~/.rvm/scripts/rvm
    rvm requirements    # 这一步安装rvm所依赖的一些包
    rvm install ruby-1.9.3   # 安装ruby
    rvm use 1.9.3
    gem update
    sudo apt-get install ruby-dev
    git clone https://github.com/imathis/octopress.git ~/myblog
    cd ~/myblog  # 输入yes
    gem install bundler
    bundle install 
    rake install

然后去github创建一个repo名为`username.github.io`，

    cd source
    rake setup_github_pages   # 输入repo地址
    rake generate && rake deploy

再访问`http://username.github.io`应该就有一个基本博客了。这时看看myblog里面的内容，source文件夹里面是我们平时操作的地方，public是根据你的代码生成的静态页面，别人访问你的网站的内容都是在这里面。而我们还应该把代码都放到github上去，以后才可以恢复：

    cd ~/myblog
    git add .
    git commit -a -m 'init'
    git push origin source

这样代码就都放到source这个branch去了，而publc或者_deploy文件夹不会push上去（因为`.gitignore`已经不让它们上传）。而你以后写文章什么的包括`rake generate/deploy`都在source文件夹里，要保存新修改的代码就回到根目录commit再push一下，以后恢复时才能保证是最新的。（之前就很纳闷为什么有时候`rake deploy`了github上的有些文件还是很久之前的样子= =）  
如果你是按照上面这样搭建的，在一个新系统中要恢复应该是这样：

    git clone -b source git@github.com:username/username.github.io.git myblog
    cd myblog
    gem install bundler
    bundle install
    rake setup_github_pages
    git clone git@github.com:username/username.github.io.git _deploy  

这样就恢复好了，别忘了修改过source文件夹里的东西后就要回到根目录`git add, git commit, git push`   
   
这苦逼的三天。。。累感不爱。一直在终端打各种命令，颈椎都快出问题了。。。  
再上张图，纪念我折腾的青春=。= （其实有些系统是之前折腾的，而且我森森明白装系统什么的比起来已经很不折腾了）  
![zheteng](http://img1.tuchuang.org/uploads/2014/01/zheteng.jpg)
  
  
  
  
  
  
