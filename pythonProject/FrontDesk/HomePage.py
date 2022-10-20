# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/
用户名和密码都是：test_fcy
'''
from random import choice
class HomePage:
    url = "http://shop-xo.hctestedu.com/"

    class Button:
        login = ("link text","登录") #登录按钮
        goodimages = ("class name","goods-images") #首页的商品图片
    class Input:
        pass

    def __init__(self,driver):
        self.driver = driver

    def open_url(self,driver):
        #打开首页网址
        driver.get(self.url)
        return self

    def click_login(self):
        #点击首页的登录按钮
        self.driver.find_element(*self.Button.login).click()
        return self

    def random_choice_goods(self):
        #随机选择商品
        choice(self.driver.find_elements(*self.Button.goodimages)).click()
        return self