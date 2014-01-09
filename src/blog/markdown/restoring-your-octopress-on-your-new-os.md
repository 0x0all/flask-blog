date:2013-05-09
tags:octopress,github,linux,blog
title:restoring-your-octopress-on-your-new-os
<!---->
#重装系统后恢复Octopress
2013-8-8 更新：  
这篇恢复教程似乎不是很好用，主要是自己当时懂得更少，如果需要可以看看[这篇](/blog/wtf-three-days/#octopress)   
<br>
  
=========题外话==========  
前两天又折腾起系统来，Mate桌面的Mint才用了一周就觉得不舒服，桌面系统经常会卡，有时点关机就直接卡在壁纸那个画面了。于是它成了我linux生涯里最短命的一个系统了。  
然后对于fedora是垂涎已久，于是下了fedora18的镜像（19已出，但不是stable的还是先算了--）。刻录好U盘后启动却有错误，google后就把里面isolinux.cfg和syslinux.cfg的两个参数改了。  
再进依然有错误。不解，便下了网络安装版，但我似乎高估了上交源和中大网络，四个小时居然只装了五百个包（一共两千多个）。于是强制终止，果然终止后什么系统也进不去了，这时还得靠室友的Cinnamon版Mint启动盘来补救。  
不甘心的我去其他地方下了fedora18再刻录，这次okay了，进入到了安装界面了。装到一半我以为终于要搞定时提示 " an unknown error has occurred "...详细信息是什么raise bootloadererror....不解。  
<!--more-->
Google无解，便下了4.3G大的硬盘版fedora（上交的镜像站对中大来说速度还是很不错的，有两三M每秒）。下完才去搜索怎么装，结果网上的教程好复杂，太懒了于是我又舍弃硬盘法=。=  
然后有下了fedora 17（网上有人说那个bootloadererror是18才有的），结果安装过程又出现一个bootloadererror！于是我彻底放弃了，恢复Cinnamon版Mint后乖乖配置回我之前的样子= =  
这两天装了好多好多次系统（包括fedora和mint）。我本人是十分赞同“生命在于折腾”的，但是折腾无果的滋味还真是难受呀。。。T_T  
=========回到正题========  

之前安装mate版mint后就试过在新系统恢复博客。由于对git和ruby这些东西的不熟，那次花了一天来恢复都失败了，而且网上说这个的很少，大都是教你怎么建立而很少说到恢复的。最终我把repo删了从头开始配置博客=。= 好在有把之前博客的文件夹留着。  
这次有了上次的经验就容易多了。下面直接记下从全新系统开始，恢复博客的过程：  
  
首先，安装git相关工具：

    sudo apt-get install git, git-core

安装ruby 和 rvm 等, 参考了<a href="http://www.verydemo.com/demo_c167_i2736.html" target="_blank">这里</a>

    sudo apt-get install curl
    curl -L get.rvm.io | bash -s stable  # 安装rvm
    source ~/.rvm/scripts/rvm
    rvm requirements    # 这一步安装rvm所依赖的一些包
    rvm install ruby-1.9.3   # 安装ruby
    rvm use 1.9.3
    gem update
    sudo apt-get install ruby-dev-tools  # 这一步也是必须的，否则后面bundle install 要出错

然后配置git和github账户：

    cd ~/.ssh
    sh-keygen -t rsa -C "your@email.com"    # 然后基本都是直接回车

然后打开.ssh里面一个.pub文件，把里面所有内容复制后去<a href="https://github.com/settings/ssh" target="_blank">这里</a>配置SSH key。  
然后，开始恢复你的blog：

    git clone -b source git@github.com:username/username.github.com.git octopress  # 这里要填上你的blog那个repo的地址
    cd octopress   # 这时弹出rvm相关信息，写yes
    git clone -b master git@github.com:username/username.github.com.git _deploy
    gem install bundler
    bundle install

这时候如果没报错就已经恢复好了。但实际上却有点不一样，我不知道是不是只有我才会，这时候我的source里面那些文章和 _include/custom/asides等文件夹里该有的东西都没有。  
也就是说如果你rake generate && rake deploy 那你的博客可能会什么都不剩，不仅是文章，连辛苦配置的侧边栏等等东西都没有了！我也不知道为什么github上的东西没有保持最新。可能又是我对github和rake不了解吧。  
还好我把之前系统的博客文件夹整个留下来了，这时我就把新恢复的整个文件夹都删了（不是整个rm -rf，而是打开文件夹把里面可见的东西删了，不包括隐藏文件！），然后把之前备份的文件夹里面可见的目录和文件都拷贝到新的那个文件夹里面。  
可能会出一些意外情况比如找不到某css文件神码的，这时自己看情况调整下啦。  
然后

    rake generate
    rake deploy

再去看，博客基本就成功迁移到你的新系统里啦。  

####最后
其实不同人可能有各自特殊的情况，可能你不用像我这般痛苦来恢复。可能你像我这样操作后离你原来的博客还有很大差距。  
这时只有多多google多多折腾啦，有了一次成功经历后记得像我现在这样记录下来。不折腾不进步，不折腾不幸福。:P  
只要整个文件夹有备份着，一切就都有希望嘛，大不了跟我之前一样整个repo删掉重头搭起 :D
   
   
---
转载请注明出处，谢谢!
