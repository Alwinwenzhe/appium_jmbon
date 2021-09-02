# -*- coding:UTF-8 -*-
from page.login import Login
from page.home import Home
from time import sleep


class Login_business(object):

    def __init__(self,i):
        self.l = Login(i)
        self.h = Home(i)

    def login(self):
        '''登录操作'''
        self.h.click_mine_e()
        self.l.click_acount_pwd()
        self.l.send_username_e('18888886140')
        self.l.send_passwd_e('jmbon888889')
        self.l.click_treaty()
        self.l.click_login_button_e()
        sleep(2)
        if self.l.get_pwd_error() == '账号或密码错误':
            return True
        else:
            return False

