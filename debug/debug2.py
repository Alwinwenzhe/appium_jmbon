import unittest
import threading
import time


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName="runTest", param=None):
        super(ParameTestCase, self).__init__(methodName)
        self.param = param
        global params
        params = param
        print('重写构造方法中的params：',params)

class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("这个是setupclass里面的参数:", params)

    def setUp(self):
        print("this is setup")

    def test_01(self):
        print("这个是测试方法里面的：", self.param)
        time.sleep(3)

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is class teardown")

def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_02", param=i))
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    threads = []
    for i in range(2):
        print(">>>>>>>>>>>>>>"+str(i))
        t = threading.Thread(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()