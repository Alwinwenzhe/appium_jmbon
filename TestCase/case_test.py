# -*- coding:UTF-8 -*-
import unittest,HTMLTestRunner, multiprocessing, time
from business.login_b import Login_business
from util.serverr import Serverv
from util.write_user_command import WriteUserCommand
from base.base_driver import BaseDriver

class ParameTestCase(unittest.TestCase):
    '''重写构造方法'''
    def __init__(self,methodName='runTest',param=None):
        super(ParameTestCase,self).__init__(methodName)
        ParameTestCase.parames = param
        print('重写构造方法：', ParameTestCase.parames)

class CaseTest(ParameTestCase):

    @classmethod
    def setUpClass(cls):
        '''appium服务调用'''
        cls.l = Login_business(ParameTestCase.parames)
        print('setupclass中的参数：',ParameTestCase.parames)

    @classmethod
    def tearDownClass(cls):
        '''整个环境清理'''
        print('清理掉所有环境信息，如：断开数据库连接等')

    def setUp(self):
        '''用例环境准备'''
        print("setup里面的参数i ：", ParameTestCase.parames)
        print('准备用例执行前的工作，如：回到首页等')

    def tearDown(self):
        '''用例环境清理'''
        print('清理用例执行后的工作')

    def test_01(self):
        '''登录用例判定运行结果'''
        print("testcase里面的参数：",ParameTestCase.parames)
        self.assertTrue(self.l.login())


def appium_init():
    '''初始化appium服务'''
    server = Serverv()
    server.start_appium_server_thread()

def get_user_info():
    '''获取设备数'''
    wu =WriteUserCommand()
    user_info = wu.get_count()
    return user_info

def get_suite(i):
    print("get_suite里面的：",i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", param=i))
    unittest.TextTestRunner().run(suite)
    # report_path = '..\\reprot\\test_report.htlm'
    # with open(report_path, 'wb') as file_object:        # 表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件
    #     HTMLTestRunner.HTMLTestRunner(file_object).run(suit)

if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_user_info()):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)
