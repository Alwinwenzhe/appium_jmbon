# #数据驱动
# #代码驱动
# #关键字驱动
# import parameterized, unittest, BeautifulReport
#
# data =[ ['http//171.0.0.0.0/8899/login','post',{'usernanme':'黑', 'passwd':'12344'}],['http//171.0.0.0.0/8899/login','post',{'usernanme': '黑', 'passwd':'12344'}],
# ]
# data = [
#     ['admin','123456',True,'正常登录'],
#     ['admin','112245',False,'冻结用户登录'],
#     ['sdfsdf','111123',False,'黑名单用户登录']
# ]
# data2 = [
#     ['admin','123456',True],
#     ['admin','1122',False],
#     ['sdfsdf','1111',False]
# ]
# def login(user,password):
#     if user=='admin' and password=='123456':
#         return True
#     return False
#
# class LoginTest(unittest.TestCase):
#
#     @parameterized.parameterized.expand(data)
#     def test_login(self,user,password,expect,desc): #四个参数正好对应二维数组四个字段
#         self._testMethodDoc = desc #自己指定的描述
#         result = login(user,password)
#         self.assertEqual(expect,result)
#
#     @parameterized.parameterized.expand(data2)
#     def test_login2(self,user,password,expect):
#         '''登录'''
#         result = login(user,password)
#         self.assertEqual(expect,result)
#
#
