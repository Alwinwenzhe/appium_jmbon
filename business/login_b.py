# -*- coding:UTF-8 -*-
from page.login import Login
from page.home import Home
from time import sleep


class Login_business(object):

    def __init__(self,i):
        self.l = Login(i)
        self.h = Home(i)

    def to_login(self):
        '''去登录界面'''
        self.h.click_mine_e()
        self.l.click_login()
        self.l.click_acount_pwd()

    def login_001(self,mobile,code,expect_text):
        '''快捷登录'''
        self.h.click_mine_e()
        self.l.send_shotcut_username_e(mobile)
        self.l.click_treaty()
        self.l.click_shotcut_verifycode()
        self.l.input_verify_code(code)
        if self.l.get_toast(expect_text):
            return True
        else:
            return False

    def login_002(self, mobile, pwd, expcet_text):
        '''登录操作'''
        self.l.send_username_e(mobile)
        self.l.send_passwd_e(pwd)
        self.l.click_treaty()
        self.l.click_login_button_e()
        sleep(2)
        if expcet_text == '欢迎回来':
            welcome = self.l.get_toast(expcet_text)
            if welcome == '欢迎回来':
                return True
            else:
                return False
        else:
            if self.l.get_pwd_error() == expcet_text:
                return False
            else:
                return True

    def access_circle(self):
        '''通过我的--最近浏览--进入圈子聊天'''
        self.h.click_mine_e()
        sleep(1)
        self.h.click_view_circle_one()
        sleep(3)


