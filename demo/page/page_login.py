from demo import page

from demo.base.base_page import BasePage


class PageLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 封装点击搜索框
    def click_search(self):
        self.click_element(page.search_btn)

    # 封装搜索框输入内容
    def search_input(self, text):
        self.input_text(page.search_input, text)

    # 封装点击返回按钮
    def click_back(self):
        self.click_element(page.back_btn)

    # 业务方法封装
    def setting_proxy(self, text):
        self.click_search()
        self.search_input(text)
        self.click_back()
