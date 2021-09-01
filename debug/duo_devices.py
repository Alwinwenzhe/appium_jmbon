# from appium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# import yaml #导入yaml
# from time import ctime
# import multiprocessing #导入多进程模块
# from util import find_devices
#
# file=open('desired_caps.yaml','r') #yaml和脚本文件处于同一个文件夹下，故直接引用文件即可；‘r’表示读取的意思
#
# data=yaml.load(file)
#
# devices_list= find_devices() #启动多个模拟器
# desired_caps =[]
#
# def appium_desire(udid,port):
#     desired_caps={} #定义字段desired_caps{}；下面开始定义字段的具体对象
#     desired_caps['platformName']=data['platformName']
#     desired_caps['platformVersion']=data['platformVersion']
#     desired_caps['deviceName']=data['deviceName'] #第一个模拟器默认127.0.0.1:62001 第二个默认：127.0.0.1:62025
#     desired_caps['udid']=udid
#     desired_caps['app']=data['app']
#     desired_caps['packageName']=data['packageName']
#     desired_caps['appActivity']=data['appActivity']
#     desired_caps['unicodekeyboard']=data['unicodekeyboard']
#     desired_caps['resetkeyboard']=data['resetkeyboard']
#     #控制台输入appium的端口号、设备的UDID和当前的时间
#     print('appium port:%s star run %s at %s' %(port,udid,ctime()))
#     driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
#     #构建desired进程组，由于有多个进行，所以进程定义成列表
#     desired_process=[]
#     #加载desired进程
#     for i in range(len(devices_list)):
#         port=4723+2*i #第一个端口号是4723，第二个是4725
#         desired=multiprocessing.Process(target=appium_desire,args=(devices_list[i],port))
#         desired_process.append(desired)
#
# if __name__ == '__main__':
#     #同时启动多设备执行测试
#     for desired in desired_process:
#         desired.start() #每个进程去启动
#         for desired in desired_process:
#         desired.join() #等所有子进程都执行完后再去关闭