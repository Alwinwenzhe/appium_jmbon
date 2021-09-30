# -*- coding:UTF-8 -*-
from base.base_driver import BaseDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(object):

    def __init__(self,i):
        self.d = i

    # 001 快捷登录
    def click_acount_pwd(self):
        '''从快捷登录中点击账号密码登录'''
        self.d.find_element_by_id('com.jmbon.android:id/text_use_other').click()        # 还原为旧得运行方式
        # self.d.click_element((By.ID, 'com.jmbon.android:id/text_use_other'))

    def send_shotcut_username_e(self,mobile):
        '''快捷登录种，手机号输入'''
        mob = self.d.find_element_by_id('com.jmbon.android:id/edit_phone')
        mob.clear()
        mob.send_keys(mobile)

    def click_shotcut_verifycode(self):
        '''快捷登录中，点击获取验证码'''
        self.d.find_element_by_id("com.jmbon.android:id/sb_get_captcha").click()

    def input_verify_code(self,code):
        '''
        输入6位验证码
        错误提示：手机验证码错误
        :return:
        '''
        self.d.find_element_by_id('com.jmbon.android:id/splitEditText').send_keys(code)

    # 002账号密码登录界面
    def send_username_e(self,mobile):
        '''获取输入手机号框'''
        # mob = self.d.find_element_by_id('com.jmbon.android:id/edit_phone')              # 还原为旧得运行方式
        # mob.clear()
        # mob.send_keys(mobile)
        self.d.input_text((By.ID, 'com.jmbon.android:id/edit_phone'),mobile)

    def send_passwd_e(self,pwd):
        '''输入密码'''
        passwd = self.d.find_element_by_id('com.jmbon.android:id/edit_passwd')
        passwd.clear()
        passwd.send_keys(pwd)
        # self.d.input_text((By.ID, 'com.jmbon.android:id/edit_passwd'),pwd)

    def click_check_passwd_e(self):
        '''点击可视密码对象'''
        self.d.find_element_by_id('com.jmbon.android:id/image_see_pass').click()
        # self.d.click_element((By.ID, 'com.jmbon.android:id/image_see_pass'))

    def click_login_button_e(self):
        '''点击登录按钮对象'''
        self.d.find_element_by_id('com.jmbon.android:id/sb_login').click()
        # self.d.click_element((By.ID, 'com.jmbon.android:id/sb_login'))

    def click_forget_pwd(self):
        '''点击忘记密码对象'''
        self.d.find_element_by_id('com.jmbon.android:id/text_retrieve_password').click()

    def click_treaty(self):
        '''点击同意协议按钮'''
        self.d.find_element_by_id("com.jmbon.android:id/check_view").click()
        # self.d.click_element((By.ID, "com.jmbon.android:id/check_view"))

    def get_pwd_error(self):

        '''
        返回账号或密码错误提示的文本信息
        :return:
        '''
        return self.d.find_element_by_id('com.jmbon.android:id/textPassError').text
        # return self.d.get_assert_text((By.ID, 'com.jmbon.android:id/textPassError'))

    def get_toast(self,error_mess):
        '''
        被base.py中方法替代了
        :param error_mess:
        :return:
        '''
        toast_ele = ("xpath", "//*[contains(@text," + error_mess + ")]")
        toast_element = WebDriverWait(self.d, 8, poll_frequency=0.5).until(EC.presence_of_element_located(toast_ele))
        return toast_element

if __name__ == '__main__':
    l = Login()
