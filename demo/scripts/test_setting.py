import pytest
import sys
import os
#因为配置文件运行及输入pytest后不找到demo包，所以要将当前目录加入到系统变量
sys.path.append(os.getcwd())
from demo.tool.util import DriverUtil

from demo.page.page_login import PageLogin


class TestSetting(object):
    def setup(self):
        #再次获取driver对象
        self.driver = DriverUtil.get_driver()
        #创建page对象将driver传入
        self.page_login = PageLogin(self.driver)

    def teardown(self):
        #这么写肯定错误
        # self.page_login.driver.quit()
        #必须这样写，因为这样driver才能置空，driver必须置空
        DriverUtil.quit_driver()
    #参数化，一个参数两个值，会运行两次
    @pytest.mark.parametrize("text", ["hello","nihao"])
    def test_setting(self, text):
        self.page_login.setting_proxy(text)


# if __name__ == '__main__':
#     pytest.main('-s page_login.py')
