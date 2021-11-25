# -- coding:utf-8 --
# -*- coding:UTF-8 -*-
from page.login import Login
from page.home import Home
from page.circle_chat import CircleChat
from page.home import Home
from page.mine import Mine
from time import sleep


class CircleChatB(object):

    def __init__(self,i):
        self.cc = CircleChat(i)
        self.h = Home(i)
        self.m = Mine(i)

    def enter_circle_susceptible_chat_and_return(self,cont):
        '''最近浏览--进入圈子聊天--发送消息--并返回我的，给出状态码'''
        sleep(1)
        self.cc.chat_cont(cont)
        self.cc.send_cont()
        send_status = self.cc.verify_send_status()
        sleep(1)
        if send_status:
            return True
        else:
            return False



