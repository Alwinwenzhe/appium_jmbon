# -- coding:utf-8 --

# unitest 批量执行case，暂不可用

import unittest
import os, datetime, time, multiprocessing
from BeautifulReport import BeautifulReport
from util.write_user_command import WriteUserCommand
from util.serverr import Serverv
from HTMLTestRunner import HTMLTestRunner

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

def get_user_info():
    '''获取设备数'''
    user_info = wu.get_count()
    return user_info

def get_suite(i):
    print("get_suite里面的：",i)
    # suite = unittest.TestSuite()
    # suite.addTest(CaseTest001("test_001", param=i))
    # unittest.TextTestRunner().run(suite)
    # 获取路径，有异常
    # project_dir = os.path.abspath(os.path.dirname(__file__))
    # report_path = project_dir + r'\report\test_report.html'
    # report_path=r'E:\python_code\alwin\appium_jmbon\report\test_report.html'
    # with open(report_path, 'wb') as file_object:        # 表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件
    #     HTMLTestRunner.HTMLTestRunner(stream=file_object,title=u'自动化测试报告',description=u'用例执行情况:').run(suite)

    root_dir = os.path.dirname(os.getcwd())      # 当前目录即根目录
    test_dir = os.path.join(root_dir + r'\TestCase')        #合并
    report_dir = os.path.join(root_dir + r'\report')

    discover = unittest.defaultTestLoader.discover(test_dir, 'test_case_*.py',None)     # test_dir--执行用例目录;test_case_*.py--匹配脚本名字；None--顶层目录名字
    now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    filename = '测试报告' + str(now)
    BeautifulReport(discover).report(description='jmbon_app_test', filename=filename, log_path=report_dir)

if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_user_info()):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)

