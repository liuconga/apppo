from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 设置缺省参数默认值，这样变的灵活，调用者可以传入自己需要的某个元素的刷新频率值或超时时间
    # 调用者不传入就走默认
    def find_el(self, loc, timeout=30, poll=0.5):
        """通过显示等待封装查找元素方法"""
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(*loc))

    def input_text(self, loc, text):
        """封装输入文本方法"""
        # 调用find_el()查找元素
        el = self.find_el(loc)
        # 输入内容前要先清空
        el.clear()
        # 输入内容
        el.send_keys(text)

    def click_element(self, loc):
        """封装元素点击方法"""
        # 调用find_el()查找元素
        self.find_el(loc).click()
