# -*- coding:UTF-8 -*-
from base.base_driver import BaseDriver
class Home(object):

    def __init__(self,i):
        bd = BaseDriver()
        self.d = bd.android_driver(i)

    def get_mine_e(self):
        '''
        获取我的元素
        :return:
        '''
        return self.d.find_element_by_id('com.jmbon.android:id/rb_mine')
