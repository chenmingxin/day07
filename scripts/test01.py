from appium import webdriver

# server 启动参数
from selenium.webdriver.common.by import By

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

"""
    目标：回顾find_element()
    说明：
        driver.find_element_by_xxx 底层调用的都是find_element()方法
"""
