date:2013-10-12
tags:javascript,canvas,tornado,html5,weibo
title:visual-weibo-relations
<!---->
#可视化微博关系
之前一直想用`three.js`做个什么东西，稍稍看了点教程发现js基础还不行 - - 于是想还是从`canvas`开始学吧。于是在[这个网站](http://www.html5canvastutorials.com)看简单的教程（不过国内访问真心慢），看了两三天就想动手干了，因为知道自己要做什么，就是将微博上的好友关系可视化一下，还要让它动起来。  
后端的话就使用`Tornado`，一直想在SAE上试试`tornado`，[这儿](http://gettingstarted.sinaapp.com/introduction.html)的教程还不错。主要是第一次在SAE使用上`mysql`，没有里面的代码示例还真不知道怎么开始。  
<!--more-->
`canvas`动画的话网上很多，我当时借鉴了[这个](http://spielzeugz.de/html5/liquid-particles.html)，当时真的很意外，原来能做到这么流畅。后来我也确实看它的源码学到了不少～  
一开始是处理微博授权问题，之前一直不明白为什么有的第三方网页应用可以在登录授权后立马进去应用页面了。一般来说，授权后是获得含有`code`的链接，通过这个`code`才能获取`access token`，然而刚刚说的情况看起来就好像跳过了输入“`code`获取`token`”的过程。后来通过`firebug`去抓其中一个应用来看，才发现在登录后有个重定向的过程。具体没有细看，但我已经大致知道怎么做了：将授权回调地址改为其中一个子页面，再在后台专门对这个页面进行处理，比如获取`url`中的`code`，再换取`token`，若成功再重定向到应用页面。至于那些使用官方`jssdk`的是不是这样我不知道（也不大会用官方这个东西，还要绑定域名才能使用，绑定域名就要备案 - - ，干脆不折腾了），反正我最后就是这样处理的。  
然后先处理canvas的东东了，一开始只是尝试在上面draw出多个image object都出问题，大概是跟图片的加载顺序/速度有关。最后在StackOverflow解决（最近好多好多问题都是靠SO，终于明白它有多好了，自己也开始尝试在上面回答问题了 ^ ^），然后发现图片尺寸和预期的差很多，扭曲严重。搞了很久才知道设置canvas长宽时有问题，应该这样子：  

    context.canvas.width = 1000;
    canvas.width = 1000;    // 不能这样
  
具体原因SO也有解释，不过看不大明白。。于是终于可以draw多图了，又去后台设置了下，把登录用户近期的评论对象（处理json数据挺麻烦的，因为有的是直接评论有的是回复评论什么的）的头像url 以字符串形式传到前端。然后按照早就设想好的，要把这些头像摆成一个圆。这点一开始真不知道怎么做，还以为要回到高中解析几何的时代去算一堆坐标 = = 后来忘记在哪里看到的一段js代码，可以让指定文字时刻围绕着鼠标指针成一个圆形。于是分析了那段代码，把文字排列成圆形的重点分离出来，再应用到自己代码上去，头像就这样排好了。老实说这个过程没那么顺利，中间有好多要微调的东西，比如半径，中心点坐标等等。  
<img src='http://img3.tuchuang.org/uploads/2014/01/gravatars-around.png' width='700px;'>  
然后当晚一鼓作气，设置了`setInterval()`函数，每隔一定的很短的时间，每个image就随机地微微变一下自己的坐标，而指定的图片就按一定比例往中心靠近。在靠近这个过程上我以为我还是不可避免要使用坐标计算了，后来发现直接使用三角函数让它的横纵坐标变化就可以了 ^ ^ 。 不过同样没有那么顺利，太久没玩数学了`sin`，`cos`一开始居然在逻辑上都会搞错 -。-   
<img src='http://img2.picbed.org/uploads/2014/01/gravatars-move.png' width='700px;'>  
后来在[这个](http://tutorials.jenkov.com/html5-canvas/animation.html)教程上学到了`animate`函数，而且能成功替代`setInterval`，结果上看貌似动起来也比后者光滑，但我纠结很久还是使用了`setInterval`，因为`animate`貌似很难设置速度，有点偏快了。  
然后又在每个图像外部添加了circle，本来希望圆形比头像小的，然后圆以外的图像部分不显示出来。但这点死活没成功，所以放弃了。。一大遗憾。最后再加上连线和颜色就基本完成了。  
<img src='http://img4.tuchuang.org/uploads/2014/01/gravatars-final.png' width='700px;'>  
这次算是从0基础的canvas开始，有个idea，逐步google写出来的。虽然有很多不足，但个人已经很满意了。`HTML5 + js` 确实是好东西啊～希望接下来能试试`three.js`，嘿嘿。  
然后这个应用前两天很顺利通过了新浪的审核，所以就上线了～～ 真心求测试啊，地址在[这里](http://vrelations.sinaapp.com) 。  
代码可以在[Github](https://github.com/yakiang/Visual-weibo-relations) 找到 ：）
