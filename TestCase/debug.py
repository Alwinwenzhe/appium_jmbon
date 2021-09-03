from util.write_user_command import WriteUserCommand
import os, time

wu = WriteUserCommand()

def swtich_default_input():
    '''切换回默认输入法'''
    device_name = wu.get_yaml('user_info_{}'.format(str(0)), 'devicesname')
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

if __name__ == '__main__':
    swtich_default_input()