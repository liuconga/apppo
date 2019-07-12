import pytest
from appium import webdriver

from v3.page.page_login import PageLogin


class TestLogin(object):
    def setup(self):
        self.page_login = PageLogin()

    def teardown(self):
         self.page_login.driver.quit()

    def test_login_username_noexists(self):
        self.page_login.login_proxy("18301225040", '123456')

    def test_login_password_error(self):
        self.page_login.login_proxy("18301225040", '8888')


pytest.main('-s test_ak_login.py')
