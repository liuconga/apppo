import os
import sys

import allure
import pytest


sys.path.append(os.getcwd())
# os.getcwd() 获取当前目录，获取绝对路径,系统目录中没有page，所有报导包错误，因为scripts跟pytest
# 的运行目录appo，并不在一级目录，所有得将当前目录加入系统路径
from v4.tool.driver_util import DriverUtil


from v4.tool.read_yaml import read_yaml
from v4.page.page_login import PageLogin

#读取yaml文件中数据
def get_data():
    result=read_yaml()
    data_list=list()
    for data in result.values():
        data_list.append(tuple(data.values()))
    return data_list


class TestLogin1(object):
    # pytest函数级别初始化
    def setup(self):
        self.driver=DriverUtil.get_driver()
        self.page_login = PageLogin(self.driver)

    # pytest类级别初始化
    def teardown(self):
        DriverUtil.quit_driver()

    # 使用pytest参数化
    # @allure.step(title='正在执行登录操作。。。。')
    # @pytest.mark.parametrize("username,password", get_data())
    def test_login(self, username=123, password=23123):

        # allure.attach("描述","hello")
        self.page_login.login_proxy(username, password)
        with open("./v4/image/1.png", 'rb')as f:
            allure.attach("失败截图", f.read(), allure.attach_type.PNG)
