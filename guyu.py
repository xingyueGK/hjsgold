# -*- coding:utf-8 -*-

import requests
import threading
import time
#import json

headers = {
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Content-Type':'application/json',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

def get_token(num,user,passwd):
    url = 'http://s{num}.game.hanjiangsanguo.com/index.php?u={user}&p={passwd}&v=0&c=login&&m=user&&token=&channel=150&lang=zh-cn&rand=150959405499450'.format(num=num,user=user,passwd=passwd)
    token = requests.session().get(url).json()
    return token['token']

class SaoDangFb(object):
    def  __init__(self,num,user,passwd):
        #随机请求参数
        self.num = num
        self.user = user
        self.passwd = passwd
        self.rand = str(int(time.time()*1000))
        self.token_uid = '210000353508'
        self.token = get_token(self.num,self.user,self.passwd)#账号密码
        #POST基础URL地址
        self.url = 'http://s{}.game.hanjiangsanguo.com/index.php?v=0&channel=150&lang=zh-cn&token={}&token_uid={}&rand={}&'.format(self.num,self.token,self.token_uid,self.rand)
    def post_url(self,data):
        for k,v in data.items():
            self.url += '&%s=%s'%(k,v)
        r = requests.post(self.url,headers=headers)
        if r.status_code != 200:
            print r.status_code
        else:
            return r.json()
    def action(self,**kwargs):
        """动作参数m={'index':'获取基础账号密码等信息',‘get_monster_list’：“获取副本怪物列表信息”}
        """
        action_data = kwargs
        serverinfo = self.post_url(action_data)
        return serverinfo
