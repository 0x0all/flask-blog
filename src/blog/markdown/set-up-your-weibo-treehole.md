date:2013-08-08
tags:python,weixin,weibo,sae
title:set-up-your-weibo-treehole
<!---->
#[微信-微博]树洞教程
同样基于SAE,使用Python实现。你得有一个SAE帐号、微信公众平台帐号和一个微博帐号。  
首先使用你那个微博帐号进入到[微博开发平台](http://open.weibo.com)，登录后要去完善开发者信息，通过邮箱认证等。再在[这里](http://open.weibo.com/development)选择创建应用，选择网页应用即可。
<!--more-->
然后出现的表格都可以随便填，不过“应用名称”不能和已有的相同。创建后到[这里](http://open.weibo.com/apps)，点击进入你的应用，点击左边的应用信息，把`Appkey`和`AppSecret`先记录下来。点击左边的高级信息，点编辑，“授权回调页”写`http://boyqiang520.s8.csome.cn/oauth2/`，“取消授权回调页”什么也不写，保存。然后打开`https://api.weibo.com/oauth2/authorize?redirect_uri=http://boyqiang520.s8.csome.cn/oauth2/&response_type=code&client_id=【1】&display=default`，其中【1】替换为刚刚保存的`Appkey`，用你那个要做树洞的微博帐号授权后页面出现一个框，把框里的内容完整复制好记录下来。再打开[这个页面](http://yakiang.sinaapp.com/getToken)，填入`appkey,appsecret`和`code`，其中`code`就是刚刚那个框里面的那串内容。提交后如果没有错误就看到两行字，先别关页面，把我这份[文件](/static/files/th-weibo.rar)下载后解压。里面有个`index.wsgi`，把第一行字填进这份文件第29行的引号内，把第二行字填进第30行，26和27行数据自己也补上。  
然后同样到[sae](http://sae.sina.com.cn/?m=myapp&a=create)创建新应用，二级域名随便写但要记住，应用名称随便写，开发语言选python。然后点击顶端“我的应用”，到你刚刚创建的应用的页面，左边栏选择“代码管理”，“创建一个版本”，默认名称为1就好。然后点击编辑代码（可能需要输入密码）进入到深蓝色那个面板。点开左边的`config.yaml`，把内容都删掉后把刚刚解压开来的文件`config.yaml`的内容复制上去，点击保存。再把面板上的`index.wsgi`右键删掉，把刚刚解压开来的另外两个文件（`index.wsgi`和`weibo.py`）上传上去（黄色箭头）。点击全部保存后可以关掉页面，回到刚刚点击“代码管理”的地方，现在点击左边栏下面的`storage`，点击新建一个domain，`domain name`写`pics`，然后下面都不写也不勾，点击创建。用同样方法再建一个domain名为`weiboid`，也就是需要两个domain。  
然后去[微信公众平台](http://mp.weixin.qq.com)，登录后进入“高级功能”，点击开发模式（使用前可能需要先去编辑模式那里把它关了），修改接口配置信息，URL就写刚刚sae的应用地址，比如`http://xxxx.sinaapp.com`，token随便写。提交，如果返回绿色消息就是提交成功了。  
至此微信-微博树洞就搭好了。功能有：发布文字和图片微博；对最近五条微博进行匿名评论和转发。  
刚刚微博应用那些其他基本应用信息（比如应用图标之类）可以不用去管它，而且不要去审核（所以发出的微博“尾巴”会是“未通过审核应用”）。  
如果你成功了，希望你能评论中留下你的学校名称。如果失败了也可以留言或者发邮件我。   
<br><br><br>
2013-10-13 更新：  
如果你不想折腾又想建树洞，而且愿意付费，欢迎找我 --- QQ 六七四六九一九三五  

