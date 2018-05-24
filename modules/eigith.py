#!/usr/bin/env python
#-*- coding:utf-8 -*-

import  matrix
from base import SaoDangFb


class eight(SaoDangFb):
    def reset(self):
        self.action(c='eight_diagram',m='reset_point')
        self.action(c='eight_diagram',m='level_index',level=1)

    def eight_index(self):
        level_index = self.action(c='eight_diagram',m='level_index',level=1)
        return level_index

    def pk(self):
        self.action(c='eight_diagram', m='pk', level=1)

    def matrix(self):
        genral_dict = {}
        matrix_index = self.action(c='matrix',m='index')
        general = matrix_index['general']
        for  k,v in general.items():
            name = v['name']
            genral_dict[name] = v['id']
        return genral_dict
    def use_matrix(self,mid=4):
        #boss固定4
        self.action(c='matrix',m='use_matrix',mid=mid)
    def update_matrix(self,uid,mid=4):
        genral_info = self.matrix()
        if [u'神孙权'] in genral_info.keys():
            lists = '%s,-1,%s,-1,%s,-1,%s,-1,%s'%(
                genral_info[u'神曹植'],
                genral_info[u'廉颇'],
                genral_info[u'阎圃'],
                genral_info[u'神孙权'],
                uid,
                )
        else:
            lists = '%s,-1,%s,-1,%s,-1,%s,-1,%s' % (
            genral_info[u'神曹植'], genral_info[u'廉颇'], genral_info[u'阎圃'], genral_info[u'神大乔'], uid)
        self.action(c='matrix',m='update_matrix',list=lists,mid=mid)

def main():

    ei = eight(num=21, user='xingyue123', passwd='413728161')
    genral = ei.matrix()
    ei.use_matrix()#使用固定阵法
    ei.update_matrix(genral[u'神刘表'])
    point = ei.eight_index()['cost']['point']
    print '当前位置',point
    if point == '9':
        ei.reset()
    for i in range(20):
        point = ei.eight_index()['cost']['point']
        if point == '7':
            # 上谋士 u'神刘表'
            ei.update_matrix(genral[u'神刘表'])
            ei.pk()
            print '当前位置', point
        elif point == '8':
            # 上武将 u'神袁尚'
            ei.update_matrix(genral[u'神袁尚'])
            ei.pk()
            print '当前位置', point
        else:
            ei.pk()
            print '当前位置', point


    ei.update_matrix(genral[u'魔张梁'])
if __name__ == '__main__':
    main()
