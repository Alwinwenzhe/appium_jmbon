# -*- coding:utf-8 -*-
import unittest, multiprocessing
import paramunittest, time
from util.write_user_command import WriteUserCommand
from util.serverr import Serverv

def appium_init():
    '''初始化appium服务'''
    server = Serverv()
    server.start_appium_server_thread()

def get_user_info():
    '''获取设备数'''
    wu =WriteUserCommand()
    user_info = wu.get_count()
    return user_info

@paramunittest.parametrized(get_user_info())
class TestBar(unittest.TestCase):
    def setParameters(self, a):
        self.i = a

    def testLess(self):
        print(self.i)

def get_suite():
    print("get_suite里面的：")
    suit = unittest.TestSuite()
    suit.addTest(TestBar('testLess'))
    unittest.TextTestRunner().run(suit)


if __name__ == "__main__":
    appium_init()
    threads = []
    for i in range(len(get_user_info())):
        t = multiprocessing.Process(target=get_suite)
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)