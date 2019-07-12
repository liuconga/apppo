"""
模块名为page开头+下划线+测试模块 如page_login
page类名：根据模块名更改而来，page_login变为大驼峰PageLogin
"""
from appium import webdriver


class PageLogin(object):
    def __init__(self):
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
        desired['appActivity'] = '.umanager.LoginActivit'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)

    # 输入手机号
    def input_username(self, username):
        el_user = self.driver.find_element_by_id('com.vcooline.aike:id/etxt_username')
        el_user.clear()
        el_user.send_keys("18301225040")

    # 输入密码
    def input_password(self, password):
        el_pw = self.driver.find_element_by_id('com.vcooline.aike:id/etxt_pwd')
        el_pw.clear()
        el_pw.send_keys("123456")

    # 点击登录
    def click_login(self):
        self.driver.find_element_by_id('com.vcooline.aike:id/btn_login').click()

    # 组合业务方法
    def login_proxy(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
