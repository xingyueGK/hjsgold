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
        self.action(c='countrymine',m='index')
        info = self.action(c='countrymine',m='caikuang',p=3,id=3,t=5)
        timeinfo = info['dateline']
        #采集矿
        if int(timeinfo) == 0 :
            self.action(c='countrymine', m='get_reward',s=3)
        else:
            time.sleep(timeinfo+10)
            self.action(c='countrymine', m='get_reward',s=3)
    def country(self):#每日国家奖励
        self.action(c='country',m='get_salary')
    def countrysacrifice(self):#每日贡献
        print self.action(c='countrysacrifice', m='index', id=1)
        print self.action(c='countrysacrifice',m='action',id=1)
def main():
    action = country(num=21, user='xingyue123', passwd='413728161')
    action.country()
    action.countrysacrifice()
    action.dice()
    for i in range(3):
        action.get_countrymine()
    action.countryboos()