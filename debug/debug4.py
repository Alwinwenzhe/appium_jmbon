# -*- coding:utf-8 -*-
import unittest
import threading
import time


class ParameTestCase(unittest.TestCase):
    #params = None
    def __init__(self, methodName="runTest",param=None):
        super(ParameTestCase,self).__init__(methodName)
        ParameTestCase.params=param
        print('重写构造方法中的params：',ParameTestCase.params)

class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("这个是setupclass里面的参数:",ParameTestCase.params)

    def setUp(self):
        print("this is setup")

    def test_01(self):
        print("这个是测试方法1里面的：",ParameTestCase.params)
        time.sleep(3)

    def test_02(self):
        print("这个是测试方法2里面的：",ParameTestCase.params)
        time.sleep(3)

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is class teardown")

def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", param=i))
    suite.addTest(CaseTest("test_02", param=i))
    unittest.TextTestRunner().run(suite)

if __name__ =='__main__':
    threads = []
    for i in range(5):
        print(">>>>>>>>>>>>>>"+str(i))
        t = threading.Thread(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()