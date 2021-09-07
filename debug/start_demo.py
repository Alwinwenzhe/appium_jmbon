#STATUS: PASS
#TIME: 2021-08-27
from appium import webdriver
from util.swip_screen import SwipScreen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



def get_driver():
    capabilities ={
        "platformName": "Android",
        "deviceName": "6JR7N16C13001252",
        "appActivity" : "com.jmbon.android.view.WelcomeActivity",        #appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
        "appPackage":"com.jmbon.android",
        "noReset":True,
        'automationName':'Uiautomator2',         # 定位toast元素就需要写
        'unicodeKeyboard':True,
        'newCommandTimeout':'150000'             # 超时设置，appium保持余设备连接
    }
    # 运行前命令行启动：appium -p 4725 -bp 5000
    driver = webdriver.Remote("http://127.0.0.1:4700/wd/hub",capabilities)
    driver.implicitly_wait(15)      # 全局设置，每个元素最长等待时间10s
    return driver

def get_toast(driver,error_mess):
    toast_ele = ("xpath","//*[contains(@text,"+ error_mess +")]")
    toast_element = WebDriverWait(driver,8,poll_frequency=0.5).until(EC.presence_of_element_located)
    return toast_element

if __name__ == '__main__':
    ss = get_driver()
    ss.find_element_by_id('com.jmbon.android:id/rb_mine').click()
    sleep(1)
    ss.find_element_by_id('com.jmbon.android:id/text_use_other').click()
    ss.find_element_by_id('com.jmbon.android:id/edit_phone').clear()
    ss.find_element_by_id('com.jmbon.android:id/edit_phone').send_keys('18888886140')
    ss.find_element_by_id('com.jmbon.android:id/edit_passwd').send_keys('jmbon888889')
    ss.find_element_by_id("com.jmbon.android:id/check_view").click()
    ss.find_element_by_id('com.jmbon.android:id/sb_login').click()
    ss.find_element(By.ID,'kw')
    sleep(6)
    ss.close_app()
    # if get_toast(ss,"账号或密码错误,请检查后重新输入"):
    #     print('pass')
    # else:
    #     print('fail')


