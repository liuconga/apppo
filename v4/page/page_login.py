"""
模块名为page开头+下划线+测试模块 如page_login
page类名：根据模块名更改而来，page_login变为大驼峰PageLogin
"""
import time

from v4 import page
from v4.base.base_page import BasePage


class PageLogin(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    # 输入手机号
    def input_username(self, username):

        self.input_text(page.user, username)

    # 输入密码
    def input_password(self, password):

        self.input_text(page.pwd, password)

    # 点击登录
    def click_login(self):
        self.click_element(page.login_btn)

    # 组合业务方法
    def login_proxy(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        time.sleep(2)

