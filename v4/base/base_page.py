from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 抽取查找元素方法
    def find_el(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 抽取输入文字方法
    def input_text(self, loc, text):
        el = self.find_el(loc)
        el.clear()
        el.send_keys(text)

    # 抽取点击操作方法
    def click_element(self, loc):
        self.find_el(loc).click()

    # 获取toast消息方法封装
    def base_get_toast_msg(self, msg):
        loc = By.XPATH, '//*[contains(@text,”{}”)]'.format(msg)
        return self.find_el(loc, poll=0.2).text
