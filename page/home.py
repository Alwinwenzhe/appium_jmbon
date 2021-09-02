# -*- coding:UTF-8 -*-
from base.base_driver import BaseDriver
class Home(object):

    def __init__(self,i):
        self.d = i

    def click_mine_e(self):
        '''
        获取我的元素
        :return:
        '''
        self.d.find_element_by_id('com.jmbon.android:id/rb_mine').click()
