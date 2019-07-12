from appium import webdriver


class DriverUtil(object):
    # 单下划线代表守护属性，类外部不能使用
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # 初始化driver
            desired = {}
            # 必填参数，且一定要正确，Android中a不区分大小写
            desired['platformName'] = 'Android'
            # 可以不填，但是要填就要填正确，跟模拟器一样或跟手机一样
            desired['platformVerison'] = '5.1'
            # Android中可以填错，但不可以为空
            desired['deviceName'] = '192.168.56.102:5555'
            # 启动时直接安装apk可以忽略下边两个包名启动名
            # desired['app'] = 'C:\\AK_CRM.apk'
            # app包名
            desired['appPackage'] = 'com.vcooline.aike'
            # app启动名
            desired['appActivity'] = '.umanager.LoginActivity'
            cls._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
