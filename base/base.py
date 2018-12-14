"""
    目标：po模式base(基类)类封装
    操作：
        1. 新建类(以大驼峰风格去编写类名)
        2. 新建公共的方法
            1. 找元素封装
            2. 输入方法封装
            3. 点击方法封装
"""

from selenium.webdriver.support.wait import WebDriverWait


# 新建类
class Base():
    def __init__(self, driver):
        self.driver = driver

    # 封装 查找元素方法
    def base_find_element(self, loc,timeout=30, poll=0.5):
        # 采用 所有定位方法的底层调用方法  find_element()
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 封装 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空操作
        el.clear()
        # 输入元素
        el.send_keys(value)

    # 封装 点击方法
    def base_click(self, loc):
        # 获取元素并点击
        self.base_find_element(loc).click()
