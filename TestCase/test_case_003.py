# # -*- coding:UTF-8 -*-
# import unittest, multiprocessing, time, os, BeautifulReport, HTMLTestRunner
# from parameterized import parameterized
# from selenium import webdriver
# from time import sleep
#
# class CaseTest001(unittest.TestCase):
#
#     def setUp(self):
#         '''用例环境准备'''
#         print('准备用例执行前的工作，如：回到首页等')
#
#     def tearDown(self):
#         '''用例环境清理'''
#         print('清理用例执行后的工作')
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.baseUrl = "http://www.baidu.com"
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#     def baidu_search(self, search_key):
#         self.driver.get(self.baseUrl)
#         self.driver.find_element_by_id("kw").send_keys(search_key)
#         self.driver.find_element_by_id("su").click()
#         sleep(2)
#
#     @parameterized.expand([
#         ("case1", "selenium"),
#         ("case1", "python"),
#         ("case1", "unittest"),
#         ("case1", "pytest"),
#     ])
#     def test_search(self, name, search_key):
#         self.baidu_search(search_key)
#         self.assertEqual(self.driver.title, search_key + "_百度搜索")
#
# def get_suite(i):
#     print("get_suite里面的：",i)
#     suite = unittest.TestSuite()
#     suite.addTest(CaseTest001("test_search"))
#
#     # # 第一，使用HTMLTestRunner方式运行
#     # report_path=r'E:\python_code\alwin\appium_jmbon\report\test_report.html'
#     # with open(report_path, 'wb') as file_object:        # 表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件
#     #     HTMLTestRunner.HTMLTestRunner(stream=file_object,title=u'自动化测试报告',description=u'用例执行情况:',verbosity=2).run(suite)
#
#     # # 第二，使用BeautifulReport方式运行
#     # path = r'E:\python_code\alwin\appium_jmbon\report'
#     # bf = BeautifulReport.BeautifulReport(suite)  # 实例化一个beatifulreport对象
#     # bf.report(filename='Jmbon_Android端测试报告',report_dir=path,description='Jmbon_Android端测试报告')  # 可使用log_path参数将报告存放到对应路径
#
#     # # 第三
#     # unittest.main(verbosity=2)  # verbosity运行结果信息复杂度 2--详细模式；verbosity运行ok
#
#     # 第四
#     suite = unittest.TestSuite()
#     suite.addTest(CaseTest001("test_search", param=i))
#     bf = BeautifulReport.BeautifulReport(suite)
#     # bf = BeautifulReport.BeautifulReport(unittest.makeSuite(suite))
#     bf.report(filename='11-17测试报告', description='接口测试报告')
#
# if __name__ == '__main__':
#     threads = []
#     for i in range(1):
#         t = multiprocessing.Process(target=get_suite, args=(i,))
#         threads.append(t)
#     for j in threads:
#         j.start()
#         time.sleep(1)