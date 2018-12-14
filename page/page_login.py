"""
    目标：PO模式page页面封装
    提示：
        1. 类名 为大驼峰模块名(去掉下划线)
        2. 每一步操作，为单独的方法
    核心：page页面对象要集成Base
"""
import page
from base.base import Base


# 创建类名
class PageLogin(Base):
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.loc_username,username)

    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.loc_password,password)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.loc_btn)

    # 封装整体登录方法 演示
    def page_login(self,username,password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()