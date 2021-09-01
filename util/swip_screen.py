# -*- coding:UTF-8 -*-
class SwipScreen(object):
    
    def __init__(self,driver):
        self.driver = driver

    # 获取屏幕宽高
    def get_size(self):
        size = self.driver.get_window_size(self)
        width = size['width']
        height = size['height']
        return width, height


    def swip_left(self):
        """
        往左滑动40%
        此方法适合在顶部banner位置进行滑动
        :return:
        """
        x = self.get_size()[0] / 10 * 8
        y = self.get_size()[1] / 10 * 2
        x1 = self.get_size()[0] / 10 * 4
        self.driver.swipe(x, y, x1, y)

    def swip_right(self):
        '''
        往右滑动40%
        :return:
        '''
        x = self.get_size()[0] / 10 * 1
        y = self.get_size()[1] / 10 * 2
        x1 = self.get_size()[0] / 10 * 9
        self.driver.swipe(x, y, x1, y)

    def swip_up(self):
        '''
        此方法是从底部往上滑动40%
        :return:
        '''
        x = self.get_size()[0] / 10 * 1
        y = self.get_size()[1] / 10 * 8
        y1 = self.get_size()[1] / 10 * 4
        self.driver.swipe(x, y, x, y1)

    def swip_down(self):
        '''
        向下滑动40%
        :return:
        '''
        x = self.get_size()[0] / 10 * 2
        y = self.get_size()[1] / 10 * 3
        y1 = self.get_size()[1] / 10 * 7
        self.driver.swipe(x, y, x, y1)

    def swip_on(self,direction):
        '''
        再次封装4个滑动方法:up,down,left,right，均滑动40%
        :return:
        '''
        if direction == 'up':
            self.swip_up(direction)
        elif direction == 'down':
            self.swip_down(direction)
        elif direction == 'left':
            self.swip_left(direction)
        elif direction == 'right':
            self.swip_right(direction)
        else:
            print('Direction error!!!')