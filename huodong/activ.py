#-*- coding:utf-8 -8-
import threading
import time

import shujufenx
from shujufenx import fuben


"""每日不定期开展活动"""
def  heishi(username,password):
    act= shujufenx.fuben(username, password)
    info = act.action(c='blackmarket',m='index')#获取黑市首页
    print info
    #refreshInfo=act.action(c='blackmarket',m='refresh')#刷新信息
    #act.action(c='blackmarket',m='buy',id=28)
def userinfo(username,password):
    act = shujufenx.fuben(username, password)
    info = act.action(c='blackmarket', m='index')  # 获取黑市首页
    memberInfo = act.action(c='member', m='index')
    name = memberInfo['nickname']#账号
    level = memberInfo['level']#等级
    act = memberInfo['act']#军令
    silver = memberInfo['silver']#银币
    gold = memberInfo['gold']#元宝

    print '账号：%s 名字：%s 等级：%s 军令：%s 银币: %s 元宝: %s 黄宝石: %s 紫宝石: %s\n---------- ' % (username,name,level,act,silver,gold,info['info']['get2'], info['info']['get3'])

def sanguo(username, password):#游历三国活动
    act = shujufenx.fuben(username, password)
    travelindex=act.action(c = 'act_travel', m = 'index')#获取活动
    details = act.action(c='act_travel', m='action_travel')['details']  # 开始活动
    print travelindex['info']['points']
    if travelindex['info']['free'] ==1:
        result = act.action(c='act_travel', m='action_dice')  # 掷骰子
    if  travelindex['info']['points'] != 0:
        # #走路顺序list[4,2,3,5,8,9,10,11,12,13,14]
        plain=[1,4,2,3,5,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        num = plain.index(int(details['current']))+1
        stats = act.action(c='act_travel',m ='plain' ,point=plain[num])
class activity(fuben):
    def haiyun(self):
        actchristmas = self.action( c = 'act_christmas' ,m = 'christmas_shop')
        shop_card = actchristmas['shop_card']#获取福卡数量
        print shop_card
        #self.action(v=0,c='act_christmas',m='exchange',id='33')#花费元宝购买
        print self.action(c='act_christmas',m='shop_buy',id=30)#用10购物卡买400紫免费
    def sign(self):#每日签到奖励
        self.action(c='sign',m='sign_index')
    def jingsu(self):#竞速奖励
        info = self.action(c='map',m='get_reward_list',channel=11,v=2017122401)
        print info
        for i in info['list']:
            if i['open_status']== 0:
                print '%s 已通过未领取 ，元宝：%s'%(i['name'],i['gold'])
            elif i['open_status']== 1:
                print '%s 未通过 ，元宝：%s' % (i['name'], i['gold'])
            elif i['open_status'] == 2:
                print '%s 已通过已领取 ，元宝：%s' % (i['name'], i['gold'])
        #self.action(c='map',m='get_mission_reward',id=120)

    def fuka(self):  # 福卡活动处理
        qm_card = self.action(c='qm_card', m='index')
        index = self.action(c='qm_card',m='get_lottery')
        print '本次花费: %s'%qm_card['cost']
        print '剩余福卡: %s'%index['lottery_num']['score']
        status = 1
        while qm_card['cost'] < '10' and status == 1:
            status = self.action(c='qm_card', m='draw ')['status']  # 随机翻牌
            print status
            qm_card = self.action(c='qm_card', m='index')

        qm_index = self.action(c='qm_card',m='get_lottery')  # 获取福卡商店首页
        qmindex = self.action(c='qm_card',m='action_lottery', id=1)  # 用福卡买1紫宝石,2突飞卡
        print qmindex
        while qmindex['status'] == 1:
            qmindex = self.action(c='qm_card',m='action_lottery',id=1)  # 用福卡买紫宝石
    def guyu(self):
        self.action(c='actguyu',m='index')
    def mooncake(self):#活动吃月饼
        self.action(c='act_mooncake',m='action',type=1)
        self.action(c='act_mooncake',m='action',type=2)
        self.action(c='act_mooncake',m='action',type=3)
    def generalpool(self):#武将池
        self.action(c='act_generalpool',m='index')
        #免费武将1谋士，2武将
        self.action(c='act_generalpool',m='lottery',type=1)
        self.action(c='act_generalpool', m='lottery', type=2)
    def messages(self):
        print  self.action(c='message',m='get_notice')
    def cuju(self):#蹴鞠首页
        index = self.action(c='act_kemari',m='index')
        for i in index['list']:
            if i['id'] == 2 and i['times'] != 0:
                self.action(c='act_kemari',m='action',type=1)
            elif i['id'] == 1 and i['times'] != 0 and i['cd'] == 0:
                self.action(c='act_kemari',m='action',type=2)
    def gongxiang(self):#国家贡献
        self.action(c='country',m='get_member_list')
        self.action(c='country',m='storage')
        print self.action(c='country',m='donate',type=1)
    def countrysacrifice(self):#国家每日贡献
        self.action(c='country',m='get_salary')
        self.action(c='countrysacrifice', m='action', id=1)
    def tes(self):#国家任务
        self.action(c='country',m='get_member_list')
        self.action(c='expostulation',m='support',id=251000004878)
    def business(self):#
        #获取通商次数
        business_times = self.action(c='business',m='index')['times']
        print '可用通商次数 %s'%business_times
        for count in range(business_times):#执行通商次数
            #每次通商是需要输入通商id
            print '开始第 %s 次通商'%count
            business_id=self.action(c='business', m='index')['trader'][0]['id']
            self.action(c='business',m='go_business',id=business_id)
        print '通商完成'
    def jinyan(self):#国家谨言
        self.action(c='expostulation',m='get_reward',id=251000004881)
    def act_sword(self):#铸剑
        self.action(c='act_sword', m='start')
        #print self.action(c='act_sword', m='battle', touid='291000034922')
        info = self.action(c='act_sword',m='index')

        self.action(c='act_sword',m='get_rank_reward',type=1)
        self.action(c='act_sword', m='get_rank_reward', type=0)
        need_nums  = int(info['need_nums'])
        nums = info['nums']
        print need_nums,nums
        #收获
        if need_nums == int(nums):
            self.action(c='act_sword', m='index')
            time.sleep(0.5)
            print self.action(c='act_sword', m='get_cast_reward')
            time.sleep(0.5)
            self.action(c='act_sword', m='index')
            self.action(c='act_sword', m='start')
        else:
            slp = need_nums - int(nums)
            print slp
            time.sleep(slp*50)
    def pack(self):#卖垃圾装备
        index = self.action(c='pack',m='index')
        # for equ in index:  # 遍历未穿戴装备列表
        #     if equ['quality'] == '3' or equ['quality'] == '1' or equ['quality'] == '2':
        #         self.action(c='pack',m='sale',id=equ['id'])
        #c=pack&m=sale&id=291000378856 ,出售制定装备
        print self.action(c='pack',m='open_box',id=5,num=40)

    def xinnian(self):  # 新年活动
        index = self.action(c='act_spring', m='sacrifice_index', v=2018021101)
        if index['price']['1']['1'] < "50":
            self.action(c='act_spring', m='sacrifice', type=1, resource_type=1)
        if index['price']['2']['1'] < "50":
            self.action(c='act_spring', m='sacrifice', type=2, resource_type=1)
        if index['price']['3']['1'] < "50":
            self.action(c='act_spring', m='sacrifice', type=3, resource_type=1)
    def leigu(self):
        self.action(c='happy_guoqing',m='get_reward',type=1)
    def fubi(self):
        status=1
        while status == 1:
            index= self.action(c='act_spring',m='exchange',id=23,v=2018021101)
            status = index['status']
    def jianghun(self):
        index = self.action(c='soul',m='index')
        info = index['pack']['list']
        memberInfo = self.action(c='member', m='index')
        name = memberInfo['nickname']  # 账号
        for  i in info:
            if i['name'] in ['穷变战魂','移山战魂','形虚战魂']:
                print '账号 ',22222
                print self.username
    def meiri(self):
        for i in range(1,16):
            print self.action(c='logined',m='get_reward',id=1)
    def chenk(self):
        self.action(c='chicken',m='vip_index',v=2018021101)
        print self.action(c='chicken', m='get_vip_reward', id=17)
        #print self.action(c='chicken', m='get_vip_reward', id=2)
        #print self.action(c='chicken', m='get_vip_reward', id=3)
        print self.action(c='act_holiday',m='index',v=2018021101)
        print self.action(c='act_holiday',m='add_login_reward',v=2018021101)
    def signs(self):#每日福利签到购买
        self.action(c='sign',m='get_reward',type=2,id=95)
    def ivlist(self):
        print self.action(c='invitation',m='change',code='nifckpm',v=2018021101)
    def shenshu(self):#神树
        index = self.action(c='sacredtree',m='index')
        if index['time'] == 1:
            print self.action(c='sacredtree',m='watering',type=1,v=2018021101)
    def yuanxiao(self):
        index = self.action(c='act_lantern',m='index',v=2018021101)
        if index['freetimes'] >0:
            self.action(c='act_lantern',m='buy',lid=1,mid=1,v=2018021101)
            self.action(c='act_lantern', m='buy', lid=1, mid=2, v=2018021101)
            self.action(c='act_lantern', m='buy', lid=1, mid=3, v=2018021101)
    def actjubao(self):
        self.action(c = 'actjubao' , m = 'index', v=2018042801)
        self.action(c = 'actjubao' , m = 'action' , type = 1 , v = 2018042801)
        self.action(c = 'actjubao' , m = 'reward_index' , v = 2018042801)
        self.action(c = 'actjubao' , m = 'get_reward' , id = 1 , v = 2018042801)
if __name__ == '__main__':
    def act(user,apass):
        action = activity(user,apass)
        #action.pack()
        #action.mooncake()
        action.cuju()
        #action.generalpool()
        #action.fuka()
        # action.messages()
    def pak(user,apass):#节节高买突飞
        action  = activity(user,apass)
        action.morra()
    def zhujian(user, apass):
        while True:
            action = activity(user, apass)
            action.act_sword()
    def xinnain(user, apass):
        action = activity(user, apass)
        action.leigu()
        action.xinnian()
        action.shenshu()
        action.yuanxiao()
    def shu(user, apass):
        action = activity(user, apass)
        action.yuanxiao()
    with open('../users/alluser.txt', 'r') as f:
        for i in f:
            str = i.strip()
            name = str + 'yue123a'
            t1 = threading.Thread(target=xinnain, args=(name,'413728161'))
            t1.start()
