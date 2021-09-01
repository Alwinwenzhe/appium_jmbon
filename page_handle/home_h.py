# -*- coding:UTF-8 -*-
from page.home import Home
from time import sleep

class HomeH(object):

    def __init__(self,i):
        self.h = Home(i)

    def click_mine(self):
        '''点击我的'''
        self.h.get_mine_e().click()
        sleep(1)


