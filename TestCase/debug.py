import csv
import codecs
import unittest, HTMLTestRunner
from time import sleep
from BeautifulReport import BeautifulReport
from itertools import islice
from selenium import webdriver
from os.path import dirname, abspath
from parameterized import parameterized


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.baseUrl = "http://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.baseUrl)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)

    @parameterized.expand([
        ("case1", "selenium"),
        ("case1", "python"),
        ("case1", "unittest"),
        ("case1", "pytest"),
    ])
    def test_search(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBaidu("test_search"))
    unittest.main(verbosity=2)         # verbosity运行结果信息复杂度 2--详细模式；verbosity运行ok

    # 第三：HTML运行异常
    # report_path = r'E:\python_code\alwin\appium_jmbon\report\test_report.html'
    # with open(report_path, 'wb') as file_object:  # 表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件
    #     HTMLTestRunner.HTMLTestRunner(stream=file_object, title=u'自动化测试报告', description=u'用例执行情况:').run(suite)
