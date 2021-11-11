# -*- coding:UTF-8 -*-
# 直接去掉多线程运行，固定在单机运行
import unittest, time, os, BeautifulReport
from business.login_b import Login_business
from util.serverr import Serverv
from util.write_user_command import WriteUserCommand
from base.base_driver import BaseDriver
from base.base import Base
from parameterized import parameterized


class CaseTest001(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''appium服务调用'''
        # cls.d = BaseDriver().android_driver(0)
        # cls.l = Login_business(cls.d)           # 将driver传递进去
        # cls.l.to_login()

    @classmethod
    def tearDownClass(cls):
        '''整个环境清理,关闭app'''
        # cls.d.close_app()
        print('清理掉所有环境信息，如：断开数据库连接等')

    def setUp(self):
        '''用例环境准备'''
        print('准备用例执行前的工作，如：回到首页等')
        self.b = BaseDriver().android_driver(0)
        self.d = Base(self.b)
        self.l = Login_business()  # 将driver传递进去


    def tearDown(self):
        '''用例环境清理'''
        swtich_default_input(0)
        self.b.close_app()
        print('清理用例执行后的工作')

    @parameterized.expand([
        [19981203720,123456,'手机验证码错误']
    ])
    def test_001(self,mobile,verify_code,expect):
        '''

        :param mobile:
        :param verify_code:
        :return:
        '''

        result = self.l.login_001(mobile,verify_code,expect)
        self.assertTrue(result)

    @parameterized.expand([
        [19981203720, 88888888, False, '账号或密码错误'],
        [15828022852, 88888888, False, '账号或密码错误'],
        [15828022852, 12345678, True, '欢迎回来']
    ])
    def test_002(self, mobile, pwd, expect, expect_text):
        '''账号密码登录'''
        print("testcase里面的参数：", self.d)
        self.l.to_login()
        result = self.l.login_002(mobile, pwd, expect_text)
        self.assertEqual(expect, result)
        time.sleep(6)

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
    bf = BeautifulReport.BeautifulReport(unittest.makeSuite(CaseTest001))  # 这里如果带参数会报错
    bf.report(filename='Jmbon_Android端测试报告', report_dir=path,
              description='Jmbon_Android端测试报告')  # 可使用log_path参数将报告存放到对应路径
