import pytest
from appium import webdriver
class TestLogin():
    def setup_class(self):
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
        desired['appActivity'] = '.umanager.LoginActivit'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)
    def teardown_class(self):
        ...

    def test_login_username_noexists(self):
        username=self.driver.find_element_by_id('com.vcooline.aike:id/etxt_username')
        username.send_keys('123123')
        pasword=self.driver.find_element_by_id('com.vcooline.aike:id/etxt_pwd')
        pasword.send_keys('123123')
        self.driver.find_element_by_id('com.vcooline.aike:id/btn_login').click()

    def test_login_password_error(self):
        username = self.driver.find_element_by_id('com.vcooline.aike:id/etxt_username')
        username.send_keys('123123')
        pasword = self.driver.find_element_by_id('com.vcooline.aike:id/etxt_pwd')
        pasword.send_keys('123123')
        self.driver.find_element_by_id('com.vcooline.aike:id/btn_login').click()



pytest.main('-s test_ak_login.py')