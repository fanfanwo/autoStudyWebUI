# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/
用户名和密码都是：test_fcy
'''
from random import choice
class GoodsInfoPage:

    class Button:
        formar_ul = ("css selector",".sku-items>ul")
        buy = ("xpath",'//button[@data-type="buy"]')

    class Input:
        pass

    def __init__(self,driver):
        self.driver = driver

    def random_choice_format(self):
        #随机选择商品规格
        ele_uls = self.driver.find_elements(*self.Button.formar_ul)
        if ele_uls:
            for i in ele_uls:
                ele_lis = i.find_elements("tag name","li")
                while True:
                    format_ = choice(ele_lis)
                    format_.click()
                    if "selected" in format_.get_attribute("class"):
                        break
        return self

    def buy_goods(self):
        #购买商品
        self.driver.find_element(*self.Button.buy).click()
        return self