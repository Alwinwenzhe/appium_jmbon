# -*- coding:UTF-8 -*-
from base.base_driver import BaseDriver
from base.base import Base
from selenium.webdriver.common.by import By


class Mine(object):
    '''我的主页'''

    def __init__(self,i):
        self.d = i

    def click_view_circle_one(self):
        '''点击最近浏览的圈子：第一个'''
        self.d.find_element_by_xpath('//*[@resource-id="com.jmbon.android:id/circleList"]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()

