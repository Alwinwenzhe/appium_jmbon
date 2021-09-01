# -*- coding:utf-8 -*-
from __future__ import division
import time
import datetime,subprocess
import unittest
import threading
from appium import webdriver
import os
import xlrd,xlwt,xlutils
from xlutils.copy import copy
from util.serverr import Serverv
import wx
from HTMLTestRunner import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'hahaha'           # 设备编码
desired_caps['appPackage'] = 'com.jmbon.android'
desired_caps['appActivity'] = 'com.jmbon.android.view.WelcomeActivity'
desired_caps["noReset"] = "true"
# desired_caps["unicodeKeyboard"] = "True"
# desired_caps["resetKeyboard"] = "True"
subprocess.Popen('killall node',shell=True)             # 杀掉之前所有appium进程
ipp = Serverv().find_devices()                                    # 设备列表
tt = []   #多线程对象

def server(ip):
    for i in range(len(ip)):                    # 设备数
        name = "./new/"+str(ipp[i])+"*****"+time.ctime()+".xls"
        SZ = xlrd.open_workbook('./new/0.xls')
        ww = copy(SZ)
        ww.save(name)
        subprocess.Popen('/Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/build/lib/main.js --address "127.0.0.1" -p "'+str(4723+2*i)+'" --command-timeout "100"  --automation-name "Appium" -U "'+ip[i]+':'+str(5555+i)+'" >/tmp/1.txt',shell=True)
        time.sleep(3.5)
        wzj = webdriver.Remote('http://localhost:'+str(4723+2*i)+'/wd/hub', desired_caps)
        dingwei = DingWei(wzj, name)
        t = threading.Thread(target=dingwei.begin)
        tt.append(t)

class DingWei():
    def __init__(self,www,fname):
        self.wzj = www
        self.num = 0
        self.fname = fname
        self.SZ = xlrd.open_workbook(self.fname)
        self.sz = self.SZ.sheet_by_name("sheet1")
        self.ww = copy(self.SZ)
        self.nrows = self.sz.nrows
    def id(self,s):
        return self.wzj.find_element_by_id(s)
    ################
    def first_start(self):
        time.sleep(4)
        for i in range(7):
            try:
                self.wzj.swipe(1000, 1500, 180, 1500)
            except:
                self.wzj.swipe(400,706,90,706)
            time.sleep(0.2)
        time.sleep(3)
        try:
            self.wzj.find_element_by_id("com.........blehunter.debug:id/bt_guide_login").click()
        except:
            pass
        time.sleep(4)
        self.id('com.........blehunter.debug:id/et_phone').send_keys('18810437161')
        self.id('com.........blehunter.debug:id/et_phone_password').send_keys('qwerty')
        self.id('com.........blehunter.debug:id/btn_login').click()
        time.sleep(5)
    def chushihua(self):
        while 1:
            if self.m.is_enabled():
                try:
                    self.id('com.........blehunter.debug:id/tv_location_failed')
                except:
                    pass
                break
            else:
                pass
    def panduan(self,no):
        while 1:
            if self.m.is_enabled():
                try :
                    self.id('com.........blehunter.debug:id/tv_location_failed')
                    self.ww.get_sheet(0).write(no+1, 1, "failed")
                    os.remove(self.fname)
                    self.ww.save(self.fname)
                except :
                    self.ww.get_sheet(0).write(no+1, 1, "success")
                    os.remove(self.fname)
                    self.ww.save(self.fname)
                    self.num += 1
                break
            else:
                pass
    def begin(self):
        #self.first_start()
        self.wzj.implicitly_wait(10)
        b = self.wzj.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView')
        b.click()
        print (self.wzj,u"初始次... ")
        self.m = self.id('com.........blehunter.debug:id/iv_refresh_friend_location')
        self.chushihua()
        j = 0
        time0 = datetime.datetime.now()
        #总次数
        n = input(u'请输入测试次数,必须为整数!')
        for i in range(n):
            j += 1
            time.sleep(1)
            time1 = datetime.datetime.now()
            self.id('com.........blehunter.debug:id/iv_refresh_friend_location').click()
            self.panduan(i)
            time2 = datetime.datetime.now()
            self.ww.get_sheet(0).write(i+1, 2, "j")
            self.ww.get_sheet(0).write(i+1, 3, str(self.num))
            self.ww.get_sheet(0).write(i+1, 4, str(j-self.num))
            self.ww.get_sheet(0).write(i+1, 5, str((time2-time1).seconds))
            self.ww.get_sheet(0).write(i+1, 6, str(int((time2-time0).seconds)-j))
            os.remove(self.fname)
            self.ww.save(self.fname)
        self.ww.get_sheet(0).write(n+2, 0,str(((self.num)/n)*100)[:6]+'%' )
        os.remove(self.fname)
        self.ww.save(self.fname)


if __name__ == "__main__":
    server(ipp)
    time.sleep(2)
    for i in tt:
        i.start()