# -*- coding:UTF-8 -*-
from page.login import Login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginH(object):

    def __init__(self,i):
        self.l = Login(i)

    def click_account_pwd(self):
        '''点击：账号密码登录'''
        self.l.get_acount_pwd().click()

    def input_username(self,mobile):
        '''输入用户名'''
        self.l.get_username_e().send_keys(mobile)

    def input_pwd(self,pwd):
        '''输入密码'''
        self.l.get_passwd_e().send_keys(pwd)

    def check_treaty(self):
        '''勾选协议'''
        self.l.get_treaty().click()

    def click_login_button(self):
        '''点击登录'''
        self.l.get_login_button_e().click()

    def get_toast(self,mes):
        '''获取toast信息'''
        self.l.get_toast(mes)

