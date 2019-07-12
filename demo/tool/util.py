from appium import webdriver
class DriverUtil(object):
    _driver = None
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            """初始化driver对象"""
            # 初始化driver
            desired = {}
            # 必填参数，且一定要正确，Android中a不区分大小写
            desired['platformName'] = 'Android'
            # 可以不填，但是要填就要填正确，跟模拟器一样或跟手机一样
            desired['platformVerison'] = '5.1'
            # Android中可以填错，但不可以为空
            desired['deviceName'] = '192.168.56.102:5555'
            # app包名
            desired['appPackage'] = 'com.android.settings'
            # app启动名
            desired['appActivity'] = '.Settings'
            cls._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)
        # 无论如何都返回driver这就是单例
        return cls._driver
    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            #必须置空,否则多个参数值会报错，因为
            cls._driver=None

if __name__ == '__main__':
    print(DriverUtil.get_driver())
    DriverUtil.quit_driver()
    print(DriverUtil.get_driver())