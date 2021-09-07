# -*- coding:UTF-8 -*-
from base.base_driver import BaseDriver
from base.base import Base
from selenium.webdriver.common.by import By


class Home(object):

    def __init__(self,i):
        self.l = i
        self.d = Base(self.l)

    def click_mine_e(self):
        '''
        点击我的元素
        :return:
        '''
        # self.d.find_element_by_id('com.jmbon.android:id/rb_mine').click()
        self.d.click_element((By.ID, 'com.jmbon.android:id/rb_mine'))