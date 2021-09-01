# -*- coding:UTF-8 -*-
from page_handle.login_h import LoginH
from page_handle.home_h import HomeH
from time import sleep


class Login_business(object):

    def __init__(self,i):
        self.l = LoginH(i)
        self.h = HomeH(i)

    def login(self):
        '''登录操作'''
        sleep(20)
        self.h.click_mine()
        self.l.click_account_pwd()
        self.l.input_username('18888886140')
        self.l.input_pwd('jmbon888889')
        self.l.check_treaty()
        self.l.click_login_button()
        sleep(6)
        if self.l.get_toast("账号或密码错误,请检查后重新输入"):
            return True

