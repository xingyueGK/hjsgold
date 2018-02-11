#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
from base import SaoDangFb

class country(SaoDangFb):
    def countryboos(self):#国家boss
        now_time = time.strftime('%H:%M:%S')
        if '20:30:00' < now_time < '20:45:00':
            boss_info = self.action(c='countryboss', m='index')
            countdown = boss_info['countdown']
            powerup = boss_info['powerup']
            if powerup != 200:
                for i in range(10):
                    self.action(c='countryboss', m='powerup', gold=0)
            while countdown > 0:
                # 获取boss退出世界
                countdown = boss_info['countdown']
                self.action(c='countryboss', m='battle')
                time.sleep(61)
            if countdown == 0:
                self.action(c='countryboss', m='reward')  # reward领取奖励
        else:
            print '国家boos未开始'
    def dice(self):#国家摇色子
        points = self.action(c='dice', m='index')['member']['points']
        if int(points) > 400:
            self.action(c='dice', m='get_reward',id=2)
        for i in range(1,8):
            self.action(c='dice',m='shake_dice')
    def get_countrymine(self):
        #收集矿
        index = self.action(c='countrymine',m='index')

        if index['log']['page'] != '0':
            print '等待收矿{}秒'.format(int(index['list'][2]['time'] + 1))
            time.sleep(int(index['list'][2]['time'] + 1))
            print self.action(c='countrymine', m='get_reward', s=3)
        else:
            info = self.action(c='countrymine',m='caikuang',p=3,id=3,t=5)
            print info
            timeinfo = info['dateline']
            #采集矿
            if int(timeinfo) == 0 :
                self.action(c='countrymine', m='get_reward',s=3)
            else:
                print '等待收矿{}秒'.format(timeinfo + 10)
                time.sleep(timeinfo + 10)
                print self.action(c='countrymine', m='get_reward',s=3)
    def country(self):#每日国家奖励
        self.action(c='country',m='get_salary')
    def countrysacrifice(self):#每日贡献
        self.action(c='countrysacrifice', m='index', id=1)
        self.action(c='countrysacrifice',m='action',id=1)
    def guoyan(self):#每日任务
        index=self.action(c='banquet',m='index')#首页
        if index['list']:
            id=index['list'][0]['caption']
            self.action(c='banquet',m='join_team',id=id)#加入宴会
        else:
            self.action(c='banquet', m='create_team', id=1)  # 创建宴会

def main():
    action = country(num=21, user='xingyue123', passwd='413728161')
    action.country()
    action.countrysacrifice()
    action.dice()
    for i in range(3):
        action.get_countrymine()
    action.countryboos()
if __name__ == '__main__':
    action = country(num=148, user='xingyue123a', passwd='413728161')
    action.get_countrymine()