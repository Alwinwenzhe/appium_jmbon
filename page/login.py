# -*- coding:UTF-8 -*-
from base.base_driver import BaseDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(object):

    def __init__(self,i):
        bd = BaseDriver()
        self.d = bd.android_driver(i)

    def get_acount_pwd(self):
        '''从快捷登录中获取账号密码登录对象'''
        return self.d.find_element_by_id('com.jmbon.android:id/text_use_other')

    def get_username_e(self,value):
        '''获取输入手机号框'''
        return self.d.find_element_by_id('com.jmbon.android:id/edit_phone')

    def get_passwd_e(self):
        '''获取密码框'''
        return  self.d.find_element_by_id('com.jmbon.android:id/edit_passwd')

    def get_check_passwd_e(self):
        '''获取可视密码对象'''
        return self.d.find_element_by_id('com.jmbon.android:id/image_see_pass')

    def get_login_button_e(self):
        '''获取登录按钮对象'''
        return self.d.find_element_by_id('com.jmbon.android:id/sb_login')

    def get_forget_pwd(self):
        '''获取忘记密码对象'''
        return self.d.find_element_by_id('com.jmbon.android:id/text_retrieve_password')

    def get_treaty(self):
        '''获取同意协议按钮'''
        return self.d.find_element_by_id("com.jmbon.android:id/check_view")


    def get_toast(self,error_mess):
        toast_ele = ("xpath", "//*[contains(@text," + error_mess + ")]")
        toast_element = WebDriverWait(self.d, 8, poll_frequency=0.5).until(EC.presence_of_element_located(toast_ele))
        return toast_element

if __name__ == '__main__':
    l = Login()
