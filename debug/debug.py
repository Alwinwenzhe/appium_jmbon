class BaseDriver(object):

    def __init__(self, i):
        self.driver = self.android_driver(i)

    def android_driver(self,i):
        print(i)

if __name__ == '__main__':
    bd = BaseDriver(0)
