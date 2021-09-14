# STATUS: PASS
# TIME: 2012-09-14

import unittest,parameterized
import BeautifulReport

data = [
    ['admin','123456',True,'正常登录'],#True为程序的预期结果，‘正常登录’表示预期结果描述用来填充报告中“用例描述”字段
    ['admin','1122',False,'冻结用户登录'],
    ['ssfss','2222',False,'黑名单用户登录']
]
#扩展：可通过excel、txt等文件来存储参数，再读入到一个二维list进行操作

def login(user,password):
    if user =='admin' and password =='123456':
        return True
    return False

if __name__ == '__main__':
    class LoginTest(unittest.TestCase):

        @parameterized.parameterized.expand(data)
        def test_login(self,username,password,expect,desc):
            self._testMethodDoc = desc #用例描述指定内容
            #登录用例                     #使用默认内容“登录用例+系统自带描述”
            result = login(username,password)
            self.assertEqual(expect,result)
    suite_case = unittest.makeSuite(LoginTest)#创建一个测试集合
    bf = BeautifulReport.BeautifulReport(suite_case)#实例化一个beatifulreport对象
    bf.report(filename='login接口测试',description='接口测试报告')#可使用log_path参数将报告存放到对应路径
