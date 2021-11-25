# -*- coding:UTF-8 -*-
# 直接去掉多线程运行，固定在单机运行
# TIME: 2021-11-18
# STAUS: PASS
#COMMENT:
import unittest, time, os, BeautifulReport
from business.login_b import Login_business
# from business.home_b import HomeH
from business.circle_chat_b import CircleChatB
from util.serverr import Serverv
from util.write_user_command import WriteUserCommand
from base.base_driver import BaseDriver
from page.home import Home
from page.mine import Mine
from parameterized import parameterized
from time import sleep

class CaseTest005(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''appium服务调用'''
        cls.d = BaseDriver().android_driver(0)
        cls.l = Login_business(cls.d)           # 将driver传递进去
        cls.cc = CircleChatB(cls.d)
        cls.h = Home(cls.d)
        cls.m = Mine(cls.d)
        sleep(1)
        cls.h.click_mine_e()
        sleep(4)
        cls.m.click_view_circle_one()

    def setUp(self):
        '''用例环境准备'''
        print('准备用例执行前的工作，如：回到首页等')

        # self.b = BaseDriver().android_driver(0)
        # self.d = Base(self.b)
        # self.l = Login_business()  # 将driver传递进去

    def tearDown(self):
        '''用例环境清理'''
        print('清理用例执行后的工作')

    @classmethod
    def tearDownClass(cls):
        '''整个环境清理,关闭app'''
        # cls.d.close_app()
        swtich_default_input(0)
        cls.d.close_app()
        print('清理掉所有环境信息，如：断开数据库连接等')

    # 敏感词测试
    @parameterized.expand([
        ['爱液'],
        ['按摩棒']
    ])
    def test_001(self, cont):
        ''''''
        sleep(3)
        result = self.cc.enter_circle_susceptible_chat_and_return(cont)
        self.assertTrue(result)
        time.sleep(1)


wu = WriteUserCommand()

def swtich_default_input(i):
    '''切换回默认输入法'''
    device_name = wu.get_yaml('user_info_{}'.format(str(i)), 'devicesname')
    os.system('adb -s {0} shell ime set {1}'.format(device_name,filter_input()[0]))
    time.sleep(1)

def filter_input():
    '''查询并返回输入法'''
    input_list = []
    result_list = os.popen('adb shell ime list -s').readlines()
    for i in result_list:
        if 'UnicodeI' in i:
            pass
        else:
            input_list.append(i)
    return input_list

def appium_init():
    '''初始化appium服务'''
    server = Serverv()
    server.start_appium_server_thread()

if __name__ == '__main__':
    appium_init()
    path = r'E:\python_code\alwin\appium_jmbon\report'
    bf = BeautifulReport.BeautifulReport(unittest.makeSuite(CaseTest005))  # 这里如果带参数会报错
    bf.report(filename='Jmbon_Android端测试报告', report_dir=path,
              description='Jmbon_Android端测试报告')  # 可使用log_path参数将报告存放到对应路径
