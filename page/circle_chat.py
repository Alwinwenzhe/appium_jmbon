# -*- coding:UTF-8 -*-
from base.base_driver import BaseDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class CircleChat(object):

    def __init__(self,i):
        self.d = i

    def chat_cont(self,cont):
        '''
        输入过敏内容
        :param cont:
        :return:
        '''
        self.d.find_element_by_id('com.jmbon.android:id/edit_comment_manager').send_keys(cont)
        sleep(3)

    def send_cont(self):
        '''点击发送按钮'''
        self.d.find_element_by_id('com.jmbon.android:id/sb_send2').click()
        sleep(1)

    def verify_send_status(self):
        '''
        获取消息发送状态
        :return:
        '''
        send_status = self.d.find_element_by_xpath('//*[@text="消息发送失败"]')
        return send_status

    def click_return(self):
        '''点击返回'''
        # self.d.tap([(100,175)],200)           # P40-坐标
        # self.d.tap([100,240],200)           # P40-pro - 坐标
        self.d.find_element_by_xpath('//android.widget.ImageButton').click()