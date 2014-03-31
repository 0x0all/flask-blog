#!/usr/bin/python
#--coding:utf-8--
import os
import sae
import urllib
import urllib2
import json
import web
import StringIO
from lxml import etree

urls = (
    '/','Weixin'
)

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)


def parse_weixin(data):
    root = etree.fromstring(data)
    child = list(root)
    rec = {}
    for c in child:
        rec[c.tag] = c.text
    return rec


def press(content, token):
    page_id = ''
    content += ' 来自微信'.decode('utf-8')
    data = {
            'v':'1.0',
            'access_token':token,
            'format':'JSON',
            'status':content.encode('utf-8'),
            'page_id':page_id, 
            'method':'status.set'
            }
    data = urllib.urlencode(data)
    url = 'https://api.renren.com/restserver.do'
    req = urllib2.Request(url, data)
    result = urllib2.urlopen(req).read()
    if 'error_code' in result:
        print result # 出错信息
        return 'error'
    return 'okay'


def refresh(rfs_token):
    client_id = ''
    client_secret = ''
    refresh_url = "https://graph.renren.com/oauth/token?grant_type=refresh_token&refresh_token=%s&client_id=%s&client_secret=%s"%(rfs_token, client_id, client_secret)
    result = urllib2.urlopen(refresh_url).read()
    result = json.loads(result)
    new_token = result['access_token']
    return new_token


def response(msg):
    textTpl = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[%s]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        <FuncFlag>0</FuncFlag>
        </xml>"""%(msg['FromUserName'], msg['ToUserName'],\
                msg['CreateTime'], 'text', msg['Content'], )
    return textTpl



class Weixin():
    def __init__(self):
        '''填入access token和refresh token'''
        self.refresh_token = ''
        self.access_token = ''
        
    def GET(self):
        '''验证微信signature'''
        data = web.input()
        return data.echostr

    def POST(self):
        '''处理微信消息'''
        data = web.data()
        msg = parse_weixin(data) # 解析微信消息
        if msg['MsgType'] == 'event' and msg['Event'] == 'subscribe':
            msg['Content'] = '欢迎添加'
        elif msg['MsgType'] == 'text':
            content = msg['Content']
            resp = press(content, self.access_token) # 发布到人人
            if resp != 'okay':
                self.access_token = refresh(self.refresh_token) # 更新token
                resp = press(content, self.access_token)
            if resp == 'okay':
                resp = '发送成功'
            else:
                resp = '发送失败'

            msg['Content'] = resp
        return response(msg) # 回复微信消息


